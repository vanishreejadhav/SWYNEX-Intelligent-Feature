import difflib

# A small FAQ knowledge base. Swap this out with your own domain later.
FAQ = {
    "what is your name": "I'm SWYNEX Bot, your friendly FAQ assistant.",
    "how do i reset my password": "Go to Settings > Account > Reset Password.",
    "what are your working hours": "We're available 9 AM to 6 PM, Monday to Friday.",
    "where are you located": "We're a fully remote, online-only service.",
    "how do i contact support": "Email us at support@example.com or use the in-app chat.",
    "what payment methods do you accept": "We accept credit cards, PayPal, and UPI.",
    "how do i cancel my subscription": "Go to Settings > Billing > Cancel Subscription.",
    "is there a free trial": "Yes, we offer a 14-day free trial with no credit card required.",
}


def get_response(user_input: str) -> str:
    """
    Intelligent feature: fuzzy-matches the user's question against the FAQ
    database using difflib, so close (but not exact) phrasing, typos, or
    reworded questions still get a correct answer. Falls back gracefully
    when no good match is found.
    """
    try:
        if not user_input or not user_input.strip():
            raise ValueError("Input is empty.")

        cleaned = user_input.strip().lower().rstrip("?!.")
        questions = list(FAQ.keys())

        # cutoff=0.6 means "60% similar or more counts as a match"
        matches = difflib.get_close_matches(cleaned, questions, n=1, cutoff=0.6)

        if matches:
            return FAQ[matches[0]]
        else:
            return (
                "I'm not sure I understand. Could you rephrase your question? "
                "Try asking about passwords, hours, support, payments, or subscriptions."
            )

    except ValueError:
        return "Please type a question — I can't respond to an empty message."
    except Exception as e:
        return f"Something went wrong while processing your question: {e}"


def chat_loop():
    """Simple command-line interface for manually chatting with the bot."""
    print("SWYNEX FAQ Bot — type 'quit' to exit.\n")
    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

        if user_input.strip().lower() == "quit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chat_loop()
