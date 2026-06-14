import json
import random
from gemini import ask_gemini
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("intents.json") as file:
    data = json.load(file)

patterns = []
tags = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

def get_response(user_input):

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, X)

    max_score = similarity.max()

    if max_score < 0.6:
        return ask_gemini(
    f"""
    You are a friendly movie recommendation chatbot.

    Keep answers under 4-5 lines.
    Be conversational.
    Recommend movies when relevant.
    Avoid long essays.

    User asked: {user_input}
    """
)

    index = similarity.argmax()

    matched_tag = tags[index]

    for intent in data["intents"]:
        if intent["tag"] == matched_tag:
            return random.choice(intent["responses"])

    return None