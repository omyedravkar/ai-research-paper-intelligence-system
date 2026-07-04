from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data.dataset_manager import get_dataframe

from search.search_engine import search

from models.summarizer import summarize
from models.keyword_extractor import extract_keywords
from models.ner import extract_entities

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

df = get_dataframe()


@app.get("/")
def home():

    return {
        "message": "AI Research Paper Intelligence System"
    }


@app.post("/search")
def search_papers(query: str):

    scores, indices = search(query)

    results = []

    for score, idx in zip(scores, indices):

        paper = df.iloc[idx]

        summary = summarize(paper["abstract"])

        keywords = extract_keywords(paper["abstract"])

        entities = extract_entities(paper["abstract"])

        results.append({

            "title": paper["title"],

            "abstract": paper["abstract"],

            "summary": summary,

            "keywords": keywords,

            "entities": entities,

            "similarity": float(score)

        })

    return results