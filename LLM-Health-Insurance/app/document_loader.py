import os
import pdfplumber
from tqdm import tqdm

POLICY_DIR = "data/policies"

def load_all_policies():
    policy_texts = {}

    for filename in tqdm(os.listdir(POLICY_DIR), desc="📂 Loading Policies"):
        if filename.endswith(".pdf"):
            path = os.path.join(POLICY_DIR, filename)
            text = extract_text_from_pdf(path)
            policy_texts[filename] = text

    return policy_texts

def extract_text_from_pdf(filepath):
    all_text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                all_text += page.extract_text() + "\n"
    except Exception as e:
        print(f"❌ Error reading {filepath}: {e}")
    return all_text.strip()
