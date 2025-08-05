from app.document_loader import load_all_policies
from app.chunker import chunk_policy_text
from app.embedder import build_faiss_index

print("📥 Loading policies...")
all_docs = load_all_policies()

# Combine and chunk all
all_chunks = []
for text in all_docs.values():
    chunks = chunk_policy_text(text)
    all_chunks.extend(chunks)

print(f"🧩 Total chunks to embed: {len(all_chunks)}")

print("🧠 Embedding and building FAISS index...")
index, texts = build_faiss_index(all_chunks)

print("✅ FAISS index built!")
print(f"🧠 Total vectors indexed: {index.ntotal}")
