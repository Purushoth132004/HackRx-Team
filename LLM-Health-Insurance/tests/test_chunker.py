from app.document_loader import load_all_policies
from app.chunker import chunk_policy_text

all_docs = load_all_policies()

for filename, text in all_docs.items():
    print(f"\n📄 {filename}")
    print("="*60)

    chunks = chunk_policy_text(text)
    print(f"🧩 Total chunks: {len(chunks)}\n")

    # Show sample chunks
    for i, chunk in enumerate(chunks[:3]):
        print(f"🧩 Chunk {i+1}:\n{chunk[:300]}...\n{'-'*40}")
