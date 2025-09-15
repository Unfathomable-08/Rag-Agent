from flask import Flask, request, jsonify
from agent import graph
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Store chat history per session_id
chat_histories = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    
    # Extract session_id and question from request
    session_id = data.get('session_id')
    question = data.get('question')
    
    if not session_id or not question:
        return jsonify({"error": "session_id and question are required"}), 400

    # Get or initialize chat history for this session
    chat_history = chat_histories.get(session_id, [])

    # Prepare input state for the graph
    input_state = {
        "session_id": session_id,
        "question": question,
        "chat_history": chat_history
    }

    # Invoke the graph with input state
    try:
        result = graph.invoke(input_state)
    except Exception as e:
        return jsonify({"error": f"Graph invocation failed: {str(e)}"}), 500

    # Update chat history
    chat_history = result.get("chat_history", chat_history)
    chat_histories[session_id] = chat_history

    # Return the bot's response
    return jsonify({
        "session_id": session_id,
        "answer": result["answer"],
        "chat_history": chat_history
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Hello! ready to chat?"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)