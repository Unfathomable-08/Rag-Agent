# RAG Agent

A Retrieval-Augmented Generation (RAG) agent built with *Flask*, *LangChain*, *Hugging Face*, and *Redis*.  
It retrieves relevant context from your dataset and generates answers using Hugging Face models.

---

## 🚀 Features
- Flask backend with /chat endpoint  
- RAG pipeline (vector search + LLM)  
- Redis as vector database  
- Configurable data source (data/product.txt)  
- Session-based chat  

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Unfathomable-08/Rag-Agent.git
cd Rag-Agent
