import spacy

# Load the spaCy model once
nlp = spacy.load("en_core_web_sm")


def extract_entities(text):

    doc = nlp(text)

    allowed = {
        "ORG",
        "PERSON",
        "PRODUCT",
        "GPE",
        "NORP",
        "EVENT",
        "WORK_OF_ART",
    }

    seen = set()
    entities = []

    for ent in doc.ents:

        if ent.label_ in allowed and ent.text not in seen:

            seen.add(ent.text)

            entities.append({
                "text": ent.text,
                "label": ent.label_
            })

    return entities