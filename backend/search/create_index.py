import os
import faiss
import numpy as np

from config.config import EMBEDDING_FILE, INDEX_FILE


def load_or_create_index():

    # If index already exists, load it
    if os.path.exists(INDEX_FILE):
        print("Loading existing FAISS index...")
        return faiss.read_index(INDEX_FILE)

    # Otherwise create it from embeddings
    print("Creating FAISS index from embeddings...")

    embeddings = np.load(EMBEDDING_FILE)

    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    # Save the index for future runs
    faiss.write_index(index, INDEX_FILE)

    print("FAISS index saved successfully!")

    return index