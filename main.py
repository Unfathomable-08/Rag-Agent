from agent import graph

chat_history = []

while True:
    question = input("You: ")

    if question.lower() in {"exit", "quit"}:
        break

    input_state = {
        "question": question,
        "chat_history": chat_history
    }

    result = graph.invoke(input_state)

    chat_history = result.get("chat_history", chat_history)

    print("Bot:", result["answer"])