import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# ✅ Load local sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Light, fast, and great for semantic search

def get_embedding(text):
    """
    Convert a text chunk to an embedding vector using local model.
    """
    return model.encode(text)

def build_faiss_index(chunks):
    """
    Convert all text chunks into embeddings and build a FAISS index.
    """
    embeddings = []
    texts = []

    for chunk in tqdm(chunks, desc="🔍 Embedding Chunks"):
        try:
            emb = get_embedding(chunk)
            embeddings.append(emb)
            texts.append(chunk)
        except Exception as e:
            print(f"❌ Embedding failed: {e}")
            continue

    if not embeddings:
        raise ValueError("No embeddings created. Check input chunks.")

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    return index, texts
