from app.document_loader import load_all_policies
from app.chunker import chunk_policy_text
from app.embedder import build_faiss_index
from app.retriever import retrieve_similar_chunks

print("📥 Loading documents...")
docs = load_all_policies()

chunks = []
for text in docs.values():
    chunks.extend(chunk_policy_text(text))

print(f"🔍 Embedding {len(chunks)} chunks...")
index, all_chunks = build_faiss_index(chunks)

# 🔎 Sample test query
query = "Is bariatric surgery covered for 45-year-old male with BMI 36 and diabetes?"

results = retrieve_similar_chunks(query, index, all_chunks, top_k=3)

print("\n🧠 Top Matching Clauses:")
for i, res in enumerate(results, 1):
    print(f"\n🔹 Match {i}:\n{res[:500]}...\n{'-'*40}")
