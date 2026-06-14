from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    bot_response = get_response(user_message)

    if bot_response is None:
        bot_response = "Sorry, I don't understand that yet."

    chat_history.append({
        "user": user_message,
        "bot": bot_response
    })

    return jsonify({
        "response": bot_response
    })

if __name__ == "__main__":
    app.run(debug=True)