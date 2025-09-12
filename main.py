from agent import graph
import uuid

chat_history = []
session_id = str(uuid.uuid4())

while True:
    question = input("You: ")

    if question.lower() in {"exit", "quit"}:
        break

    input_state = {
        "session_id": session_id,
        "question": question,
        "chat_history": chat_history
    }

    result = graph.invoke(input_state)

    chat_history = result.get("chat_history", chat_history)

    print("Bot:", result["answer"])