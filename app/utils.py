import spacy

nlp = spacy.load('en_core_web_sm')

def analyze_text(text):
    doc = nlp(text)
    return [(token.text, token.pos_, token.dep_) for token in doc]
