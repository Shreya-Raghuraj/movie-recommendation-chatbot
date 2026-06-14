from chatbot import get_response

while True:
    msg = input("You: ")

    response = get_response(msg)

    if response:
        print("Bot:", response)
    else:
        print("Bot: No intent found")