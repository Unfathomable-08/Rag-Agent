from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

def load_vectorstore():
    api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    embeddings = HuggingFaceEndpointEmbeddings(
        repo_id="sentence-transformers/all-MiniLM-L6-v2",
        task="feature-extraction",
        huggingfacehub_api_token=api_token
    )

    vectorstore = FAISS.load_local("data/faiss_index", embeddings, allow_dangerous_deserialization=True)
    return vectorstore
