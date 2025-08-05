import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def evaluate_claim(user_query: str, clauses: list):
    prompt = build_prompt(user_query, clauses)

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an expert insurance claim evaluator. Respond only in JSON."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content.strip()

    try:
        import json
        return json.loads(result)
    except Exception as e:
        print("⚠️ Couldn't parse LLM response as JSON.")
        return {"raw_response": result}


def build_prompt(user_query: str, clauses: list):
    clause_text = "\n\n---\n\n".join(clauses)

    return f"""
You are a strict insurance claim evaluator for a healthcare insurance company. The user's input is verified and factual. Your task is to evaluate the claim **only** based on the verified input and the provided clauses.

✅ Assume the user query is 100% truthful and complete.  
❌ Do not make up requirements or add missing assumptions.  
❌ Do not reject the claim unless the **clause explicitly prohibits** it.

---

🔹 User Query:
\"{user_query}\"

🔹 Retrieved Clauses:
{clause_text}

---

🎯 Respond in this strict JSON format:
{{
  "decision": "approved" or "rejected",
  "amount": "as per policy limits" or "Not applicable",
  "justification": "short explanation referring to specific clause(s)"
}}
"""
