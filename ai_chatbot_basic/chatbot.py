import json
import re

# Load the expanded JSON Q&A data
with open("qa_data.json", "r", encoding="utf-8") as file:
    qa_pairs = json.load(file)

def clean(text):
    """Basic cleaner to standardize input text"""
    return re.sub(r'[^\w\s]', '', text.lower())

def get_response(user_input):
    user_input_clean = clean(user_input)

    for pair in qa_pairs:
        question = clean(pair["question"])
        if question in user_input_clean or user_input_clean in question:
            return pair["answer"]

    # Optional fallback if no match found
    return "I'm sorry, I didn't understand that. Try asking something else!"
