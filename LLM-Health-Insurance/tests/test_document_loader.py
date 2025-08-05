from app.document_loader import load_all_policies

all_docs = load_all_policies()

for filename, content in all_docs.items():
    print(f"\n📄 {filename} - {len(content)} characters")
    print("="*60)
    print(content[:500] + "...\n")  # print preview of each doc

