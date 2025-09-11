from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def build_and_save_vectorstore():
    api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    with open("data/products.txt", "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.strip().split('\n\n')
    documents = [Document(page_content=line) for line in lines]

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(documents)

    embeddings = HuggingFaceEndpointEmbeddings(
        repo_id="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction",
        huggingfacehub_api_token=api_token
    )

    # Create FAISS vectorstore
    vectorstore = FAISS.from_documents(splits, embedding=embeddings)

    # Save to local directory
    vectorstore.save_local("data/faiss_index")
    print("FAISS vectorstore saved to disk.")

if __name__ == "__main__":
    build_and_save_vectorstore()