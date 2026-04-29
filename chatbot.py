import nltk
import random
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening", "howdy", "greetings"],
        "responses": [
            "Hello! Welcome to ShopEasy support. How can I help you today?",
            "Hi there! I'm your ShopEasy assistant. What can I do for you?",
            "Hey! Great to have you here. How may I assist you?",
        ],
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "take care", "exit", "quit", "later"],
        "responses": [
            "Goodbye! Have a wonderful day.",
            "Thanks for contacting ShopEasy. See you soon!",
            "Bye! Don't hesitate to reach out if you need anything.",
        ],
    },
    "order_status": {
        "patterns": ["order status", "where is my order", "track order", "order tracking",
                     "when will my order arrive", "delivery status", "shipment"],
        "responses": [
            "To track your order, please visit our website and enter your Order ID.",
            "You can check your order status in 'My Orders'.",
            "Share your Order ID and I'll help you track it.",
        ],
    },
    "return_policy": {
        "patterns": ["return", "refund", "exchange", "money back", "return policy",
                     "how to return", "want to return", "cancel order"],
        "responses": [
            "Returns are allowed within 30 days.",
            "Go to 'My Orders' → 'Return Item'.",
            "We offer free returns on all orders.",
        ],
    },
    "payment": {
        "patterns": ["payment", "pay", "credit card", "debit card", "upi", "net banking",
                     "payment methods", "how to pay", "payment failed", "transaction"],
        "responses": [
            "We accept cards, UPI, net banking, and COD.",
            "Retry payment or use another method.",
            "Check card details or bank restrictions.",
        ],
    },
    "discount": {
        "patterns": ["discount", "coupon", "promo code", "offer", "sale", "deal",
                     "voucher", "cashback", "savings"],
        "responses": [
            "Check our offers section.",
            "Use WELCOME10 for discount.",
            "Subscribe for latest deals.",
        ],
    },
    "product_info": {
        "patterns": ["product", "item", "specification", "details", "features",
                     "available", "stock", "color", "size"],
        "responses": [
            "Check product page for details.",
            "Share product name for help.",
            "Details are listed on product page.",
        ],
    },
    "contact_support": {
        "patterns": ["contact", "customer service", "support", "help", "agent",
                     "human", "representative", "call", "email"],
        "responses": [
            "Email support@shopeasy.com or call 1800-123-4567.",
            "Use live chat or email us.",
            "Call or chat with our support team.",
        ],
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thank", "appreciate", "helpful", "great"],
        "responses": [
            "You're welcome!",
            "Glad I could help!",
            "Happy to assist!",
        ],
    },
}

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens

def match_intent(user_tokens):
    best_intent = None
    best_score = 0

    for intent_name, data in INTENTS.items():
        score = 0
        for pattern in data["patterns"]:
            pattern_tokens = preprocess(pattern)
            matches = sum(1 for pt in pattern_tokens if pt in user_tokens)
            score = max(score, matches)

        if score > best_score:
            best_score = score
            best_intent = intent_name

    return best_intent if best_score > 0 else None

def get_response(user_input):
    tokens = preprocess(user_input)
    if not tokens:
        return "Please rephrase."

    intent = match_intent(tokens)
    if intent:
        return random.choice(INTENTS[intent]["responses"])

    return "I didn't understand. Ask about orders, payments, or returns."

def chat():
    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)
        print("Bot:", response)

        if match_intent(preprocess(user_input)) == "farewell":
            break

if __name__ == "__main__":
    chat()
