import nltk
import random
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hello!", "Hi there!", "Hey!"]
    },
    "order": {
        "patterns": ["order", "track", "status"],
        "responses": ["You can track your order in 'My Orders' section."]
    },
    "payment": {
        "patterns": ["payment", "pay", "upi"],
        "responses": ["We support UPI, cards, and COD."]
    },
    "farewell": {
        "patterns": ["bye", "exit", "quit"],
        "responses": ["Goodbye!", "See you later!"]
    }
}

stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

def match_intent(user_tokens):
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            if pattern in user_tokens:
                return intent
    return None

def get_response(user_input):
    tokens = preprocess(user_input)
    intent = match_intent(tokens)

    if intent:
        return random.choice(INTENTS[intent]["responses"])
    else:
        return "Sorry, I didn't understand."

def chat():
    print("Simple Chatbot (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

if __name__ == "__main__":
    chat()
