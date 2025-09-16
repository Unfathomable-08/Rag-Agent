RAG Agent
A Retrieval-Augmented Generation (RAG) agent built with Flask, LangChain, Hugging Face, and Redis.It retrieves relevant context from your dataset and generates answers using Hugging Face models.

🚀 Features

Flask backend with /chat endpoint  
RAG pipeline (vector search + LLM)  
Redis as vector database  
Configurable data source (data/product.txt)  
Session-based chat


📦 Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd <repo-folder>

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment
Windows
venv\Scripts\activate

Linux/Mac
source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Configure environment variables
Copy the example file:
cp .env.example .env

Open .env and fill in:

Hugging Face API Token → Get it here
Redis Cloud URL → Get it here

Example Redis URL format:
redis://default:<your-password>@<your-host>:<port>

6. Prepare data
You can keep or modify the file:
data/product.txt

7. Build the vector database
python vector_builder.py

8. Start the server
python main.py

The Flask server will start locally.

📡 API Usage
Endpoint
POST /chat

Request body
{
  "session_id": "user123",
  "question": "What products do you have?"
}

Example using curl
curl -X POST http://127.0.0.1:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id": "user123", "question": "What products do you have?"}'

Response
{
  "answer": "We have a range of products including..."
}


🛠 Tech Stack

Python 3
Flask
LangChain
Hugging Face Inference API
Redis (as vector DB)
FAISS


📖 Notes

Replace data/product.txt with your own dataset for custom answers.
Ensure Redis Cloud is running and accessible.
Hugging Face token must have inference API permissions.
