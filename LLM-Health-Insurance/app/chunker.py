import re

def chunk_policy_text(text):
    """
    Splits text into semantically meaningful chunks (clauses).
    """
    # Normalize
    text = re.sub(r'\n+', '\n', text)

    # Split using common clause patterns
    clause_patterns = [
        r'\n(?=\d+\.\s)',               # 1. Clause style
        r'\n(?=[A-Z][a-z ]{3,20}:)',     # Coverage:, Eligibility:
        r'\n(?=Exclusion\s*\d{1,2})',    # Exclusion 06
        r'\n(?=Waiting\sPeriod)',       # Waiting Period
        r'\n(?=Benefits\s*:?|Scope\s*:?|Limitations\s*:?)',
    ]

    pattern = '|'.join(clause_patterns)

    chunks = re.split(pattern, text)
    chunks = [chunk.strip() for chunk in chunks if len(chunk.strip()) > 100]

    return chunks
