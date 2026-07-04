from keybert import KeyBERT
from models.embedding_model import model

kw_model = KeyBERT(model)

def extract_keywords(text):
    return kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 3),
        stop_words="english"
    )