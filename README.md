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
git clone https:/github.com/Unfathomable-08/Rag-Agent.git
cd Rag-Agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment
**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure environment variables
Copy the example file:
```bash
cp .env.example .env
```

Open .env and fill in:

- Hugging Face API Token → Get it here
- Redis Cloud URL → Get it here

Example Redis URL format:
```bash
textredis:/default:<your-password>@<your-host>:<port>
```

### 6. Prepare data
You can keep or modify the file:
textdata/product.txt

### 7. Build the vector database
```bash
python vector_builder.py
```

### 8. Start the server
```bash
python main.py
```

The Flask server will start locally.

### 📡 API Usage
**Endpoint**
textPOST /chat

Request body
```bash
json{
  "session_id": "user123",
  "question": "What products do you have?"
}
```

Example using curl
```bash
curl -X POST http:/127.0.0.1:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "user123", "question": "What products do you have?"}'
```

Response
```bash
json{
  "answer": "We have a range of products including..."
}
```

### 🛠 Tech Stack

- Python 3
- Flask
- LangChain
- Hugging Face Inference API
- Redis (as vector DB)
- FAISS


### 📖 Notes

"""
Replace data/product.txt with your own dataset for custom answers.
Ensure Redis Cloud is running and accessible.
Hugging Face token must have inference API permissions.
"""
