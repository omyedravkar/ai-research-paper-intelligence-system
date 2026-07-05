from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = [
    "Natural Language Processing",
    "Computer Vision",
    "Machine Learning",
    "Deep Learning",
    "Healthcare AI",
    "Cyber Security",
    "Data Mining",
    "Robotics",
    "Reinforcement Learning"
]


def classify_paper(text):

    result = classifier(
        text,
        LABELS,
        multi_label=False
    )

    return {
        "category": result["labels"][0],
        "confidence": round(result["scores"][0], 3)
    }