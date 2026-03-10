import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    entities = {
        "name": None,
        "organizations": [],
        "locations": [],
        "dates": []
    }

    for ent in doc.ents:

        if ent.label_ == "PERSON":
            entities["name"] = ent.text

        if ent.label_ == "ORG":
            entities["organizations"].append(ent.text)

        if ent.label_ == "GPE":
            entities["locations"].append(ent.text)

        if ent.label_ == "DATE":
            entities["dates"].append(ent.text)

    return entities