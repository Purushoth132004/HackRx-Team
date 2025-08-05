from app.document_loader import load_all_policies
from app.chunker import chunk_policy_text
from app.embedder import build_faiss_index
from app.retriever import retrieve_similar_chunks
from app.decision_engine import evaluate_claim

# Load docs and build index
docs = load_all_policies()
chunks = []
for text in docs.values():
    chunks.extend(chunk_policy_text(text))

index, all_chunks = build_faiss_index(chunks)

# Sample test query
query = (
 "28-year-old male with BMI 33 underwent bariatric surgery without a doctor's advice. The policy has only been active for 4 months."
)


# Get relevant clauses
top_clauses = retrieve_similar_chunks(query, index, all_chunks, top_k=5)

# Evaluate decision
result = evaluate_claim(query, top_clauses)

print("\n🧾 Final Decision:")
print(result)
