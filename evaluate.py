from chatbot import get_response

# A mix of normal questions, typos, edge cases, and cases meant to break the bot
test_cases = [
    ("What is your name?", "Exact-ish match — should work well."),
    ("how do i rest my password", "Typo test — 'rest' instead of 'reset'."),
    ("What are your working hors", "Typo test — 'hors' instead of 'hours'."),
    ("", "Empty input — should trigger error handling, not crash."),
    ("Do you accept bitcoin?", "Not in FAQ — should trigger the fallback message."),
    ("cancel subscription please", "Reworded phrasing — should still fuzzy match."),
    ("asdkjfh qwoeiuqwe", "Gibberish — should trigger the fallback message."),
    ("Where are you located??", "Extra punctuation — should still match correctly."),
]


def run_evaluation():
    print("Running evaluation...\n")
    results = []
    for question, note in test_cases:
        response = get_response(question)
        results.append((question, note, response))
        print(f"Q: {question!r}")
        print(f"Note: {note}")
        print(f"Bot: {response}")
        print("-" * 50)
    return results


if __name__ == "__main__":
    run_evaluation()
