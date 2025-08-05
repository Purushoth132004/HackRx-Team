import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# 🔁 Must match model used in embedder.py
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_query_embedding(query):
    return model.encode(query)

def retrieve_similar_chunks(query, index, all_chunks, top_k=5):
    """
    Given a query, return top_k most similar chunks from FAISS index.
    """
    query_vector = get_query_embedding(query)
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(all_chunks):
            results.append(all_chunks[idx])

    return results
