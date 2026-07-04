from datasets import load_dataset
import pandas as pd

from config.config import DATASET_NAME, DATASET_SIZE


def load_papers():

    dataset = load_dataset(DATASET_NAME, split="train")

    df = pd.DataFrame(dataset)

    df = df[["title", "abstract"]]

    df = df.head(DATASET_SIZE)

    df = df.dropna()

    df["paper_text"] = df["title"] + " " + df["abstract"]

    df["paper_text"] = df["paper_text"].str.replace("\n", " ", regex=False)

    df["paper_text"] = df["paper_text"].str.strip()

    return df