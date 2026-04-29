"""
Elementary Customer Service Chatbot using NLTK
Application: E-commerce / Online Store Support
"""

import nltk
import random
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ── Download required NLTK resources ────────────────────────────────────────
nltk.download("punkt",        quiet=True)
nltk.download("punkt_tab",    quiet=True)
nltk.download("stopwords",    quiet=True)
nltk.download("wordnet",      quiet=True)

# ── Knowledge Base ───────────────────────────────────────────────────────────
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
            "Goodbye! Have a wonderful day. 😊",
            "Thanks for contacting ShopEasy. See you soon!",
            "Bye! Don't hesitate to reach out if you need anything.",
        ],
    },
    "order_status": {
        "patterns": ["order status", "where is my order", "track order", "order tracking",
                     "when will my order arrive", "delivery status", "shipment"],
        "responses": [
            "To track your order, please visit our website and enter your Order ID in the 'Track Order' section.",
            "You can check your order status by logging in to your account and going to 'My Orders'.",
            "For real-time tracking, please share your Order ID and I'll look it up for you!",
        ],
    },
    "return_policy": {
        "patterns": ["return", "refund", "exchange", "money back", "return policy",
                     "how to return", "want to return", "cancel order"],
        "responses": [
            "Our return policy allows returns within 30 days of purchase. Items must be unused and in original packaging.",
            "You can initiate a return from your account under 'My Orders' → 'Return Item'. Refunds are processed in 5–7 business days.",
            "We offer free returns on all orders! Just go to 'My Orders', select the item, and click 'Request Return'.",
        ],
    },
    "payment": {
        "patterns": ["payment", "pay", "credit card", "debit card", "upi", "net banking",
                     "payment methods", "how to pay", "payment failed", "transaction"],
        "responses": [
            "We accept Credit/Debit Cards, UPI, Net Banking, Wallets, and Cash on Delivery.",
            "If your payment failed, please retry after a few minutes or use a different payment method.",
            "For payment issues, ensure your card details are correct and your bank hasn't blocked the transaction.",
        ],
    },
    "discount": {
        "patterns": ["discount", "coupon", "promo code", "offer", "sale", "deal",
                     "voucher", "cashback", "savings"],
        "responses": [
            "Check our 'Offers' section for the latest deals and discount codes!",
            "Use code WELCOME10 for 10% off your first order. Happy shopping!",
            "We run seasonal sales often. Subscribe to our newsletter to never miss a deal!",
        ],
    },
    "product_info": {
        "patterns": ["product", "item", "specification", "details", "features",
                     "available", "stock", "color", "size"],
        "responses": [
            "You can find detailed product information on the product page. Just search for the item on our website.",
            "For stock availability or specific product queries, please share the product name and I'll help you out!",
            "All product details including size, color options, and specifications are listed on each product page.",
        ],
    },
    "contact_support": {
        "patterns": ["contact", "customer service", "support", "help", "agent",
                     "human", "representative", "call", "email"],
        "responses": [
            "You can reach our support team at support@shopeasy.com or call 1800-123-4567 (Mon–Sat, 9 AM – 6 PM).",
            "Our live chat support is available on the website. You can also email us at support@shopeasy.com.",
            "To speak with a human agent, call us at 1800-123-4567 or use the Live Chat option on our website.",
        ],
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "thank", "appreciate", "helpful", "great"],
        "responses": [
            "You're welcome! Happy to help. 😊",
            "Glad I could assist! Is there anything else you need?",
            "Anytime! Your satisfaction is our priority.",
        ],
    },
}

# ── NLP Utilities ─────────────────────────────────────────────────────────────
lemmatizer  = WordNetLemmatizer()
stop_words  = set(stopwords.words("english"))

def preprocess(text: str) -> list[str]:
    """Tokenize, lowercase, remove punctuation & stopwords, then lemmatize."""
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens

def match_intent(user_tokens: list[str]) -> str | None:
    """Return the best-matching intent name, or None if no match found."""
    best_intent = None
    best_score  = 0

    for intent_name, data in INTENTS.items():
        score = 0
        for pattern in data["patterns"]:
            pattern_tokens = preprocess(pattern)
            # Count how many pattern tokens appear in the user input
            matches = sum(1 for pt in pattern_tokens if pt in user_tokens)
            score   = max(score, matches)

        if score > best_score:
            best_score  = score
            best_intent = intent_name

    return best_intent if best_score > 0 else None

def get_response(user_input: str) -> str:
    """Return a chatbot response for the given user input."""
    tokens = preprocess(user_input)
    if not tokens:
        return "I didn't quite catch that. Could you please rephrase?"

    intent = match_intent(tokens)
    if intent:
        return random.choice(INTENTS[intent]["responses"])
    return (
        "I'm sorry, I didn't understand that. Could you try rephrasing?\n"
        "You can ask about: orders, returns, payments, discounts, or contact support."
    )

# ── Main Chat Loop ────────────────────────────────────────────────────────────
def chat():
    print("=" * 55)
    print("   🛒  ShopEasy Customer Support Chatbot")
    print("=" * 55)
    print("Type your message below. Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a great day! 👋")
            break

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Bot: {response}\n")

        # Exit on farewell
        if match_intent(preprocess(user_input)) == "farewell":
            break

if __name__ == "__main__":
    chat()
