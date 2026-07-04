from transformers import pipeline
from config.config import SUMMARY_MODEL

summarizer = pipeline(
    "summarization",
    model=SUMMARY_MODEL
)

def summarize(text):
    summary = summarizer(
        text,
        max_length=120,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]