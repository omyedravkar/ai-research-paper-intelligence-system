import faiss

from models.embedding_model import model
from search.create_index import load_or_create_index

index = load_or_create_index()


def search(query, k=5):

    query_embedding = model.encode([query])

    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(query_embedding, k)

    return distances[0], indices[0]