# entity_extraction.py
import spacy

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
sample_text = """
The Calculator module contains methods for add, subtract, multiply, and divide.
The factorial function is used recursively and depends on the math library.
"""
entities = extract_entities(sample_text)
print(entities)
