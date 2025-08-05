# streamlit_app.py

import streamlit as st
from app.query_parser import parse_health_query
from app.document_loader import load_all_policies
from app.chunker import chunk_policy_text
from app.embedder import build_faiss_index
from app.retriever import retrieve_similar_chunks
from app.decision_engine import evaluate_claim

# --- Load documents and build index once ---
@st.cache_resource
def load_index():
    docs = load_all_policies()
    chunks = []
    for text in docs.values():
        chunks.extend(chunk_policy_text(text))
    index, all_chunks = build_faiss_index(chunks)
    return index, all_chunks

index, all_chunks = load_index()

# --- Streamlit UI ---
st.title("🩺 Health Insurance Claim Evaluator")

query = st.text_area("📝 Enter your claim query (natural language)", height=150,
    placeholder="Example: 46-year-old male, BMI 36, type 2 diabetes, bariatric surgery advised by doctor, policy active 15 months")

if st.button("Evaluate Claim"):
    with st.spinner("🔍 Parsing and evaluating..."):

        # Parse and retrieve
        parsed = parse_health_query(query)
        retrieved = retrieve_similar_chunks(query, index, all_chunks, top_k=5)
        decision = evaluate_claim(query, retrieved)

    # --- Show Results ---
    st.subheader("📊 Parsed Query")
    st.json(parsed)

    st.subheader("📄 Top Matching Clauses")
    for i, clause in enumerate(retrieved, 1):
        st.markdown(f"**Clause {i}:**\n> {clause}")

    st.subheader("✅ Final Decision")
    st.json(decision)
