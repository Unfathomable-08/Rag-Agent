import os
from dotenv import load_dotenv
from typing import TypedDict, List
from langchain_core.documents import Document
from data_loader import load_vectorstore
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
from langgraph.graph import StateGraph, START, END

# Load huggingface api key
load_dotenv()
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Set up the InferenceClient
client = InferenceClient(model="mistralai/Mixtral-8x7B-Instruct-v0.1", token=api_token)

# Define prompt template
prompt_template = PromptTemplate.from_template(
    "Chat History: {chat_history}\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
)

# Load vector db
vectorstore = load_vectorstore()

# State Dictionery
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str
    chat_history: List[str] 

# Retrive node
def retrieve(state: State):
    query = state["question"]
    results = vectorstore.similarity_search(query, k=5)  # Top 5 matches
    return {"context": results}

# Generate Response Node
def generate(state: State):
    context_text = "\n\n".join(doc.page_content for doc in state["context"])

    chat_history = state.get("chat_history", [])
    chat_history_text = "\n".join(chat_history)

    formatted_input = prompt_template.format(
        question=state["question"],
        context=context_text,
        chat_history=chat_history_text or "No previous conversation."
    )

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": formatted_input}],
        max_tokens=2000,
        temperature=0.5
    )
    result = response.choices[0].message.content.strip()

    updated_history = chat_history + [
        f"User: {state['question']}",
        f"Bot: {result}"
    ]

    return {
        "answer": result,
        "chat_history": updated_history
    }


builder = StateGraph(State)
builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()