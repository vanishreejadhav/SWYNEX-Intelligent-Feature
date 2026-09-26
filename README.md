# SWYNEX Intelligent Feature — FAQ Chatbot

A simple FAQ chatbot with an added **intelligent feature**: fuzzy string matching, so it can understand typos and reworded questions instead of requiring an exact match.

## Files
- `chatbot.py` — core chatbot logic + command-line interface
- `evaluate.py` — evaluation script with normal, edge, and failure test cases
- `demo.ipynb` — notebook demo walking through the feature, evaluation, and failure analysis

## How to run

**Command line:**
```bash
python chatbot.py
```

**Evaluation:**
```bash
python evaluate.py
```

**Notebook demo:**
Open `demo.ipynb` in Jupyter or Google Colab and run all cells.

## The intelligent feature
The bot uses Python's `difflib.get_close_matches` to compare the user's question against a small FAQ knowledge base, matching even when there are typos or slightly different wording (e.g. "waht are ur hourz" still matches "what are your working hours").

## Error handling
- Empty input is caught and given a helpful prompt instead of crashing.
- Unexpected errors are caught generically so the bot never crashes mid-conversation.
- Unmatched questions get a graceful fallback message.

## Known limitations (see `demo.ipynb` for full analysis)
- Cannot handle compound questions (two topics in one message).
- Very short/keyword-only inputs sometimes fail to match.
- Matching is based on string similarity, not true semantic understanding.
