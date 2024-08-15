import spacy
from transformers import pipeline

# Load pre-trained models
nlp = spacy.load("en_core_web_sm")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_input(user_input):
    try:
        doc = nlp(user_input)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        sentiment = doc.sentiment
        intent = detect_intent(doc)
        is_command = detect_command(user_input)

        return {
            "entities": entities,
            "sentiment": sentiment,
            "intent": intent,
            "is_command": is_command
        }
    except Exception as e:
        logging.error(f"Error during input analysis: {str(e)}")
        return {"error": "Failed to analyze input"}

def detect_intent(doc):
    if any(token.dep_ == "ROOT" and token.pos_ == "VERB" for token in doc):
        return "action"
    elif any(token.tag_ == "WP" for token in doc):
        return "question"
    else:
        return "statement"

def detect_command(user_input):
    command_keywords = ["run", "execute", "command", "shell", "terminal", "bash"]
    return any(keyword in user_input.lower() for keyword in command_keywords)
