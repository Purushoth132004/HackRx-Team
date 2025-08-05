from openai import OpenAI
import os
from dotenv import load_dotenv

# ✅ Load the .env file
load_dotenv()

# ✅ Read the GROQ API key
groq_key = os.getenv("GROQ_API_KEY")

# ✅ Check that it is set
if not groq_key:
    raise ValueError("⚠️ GROQ_API_KEY not found in .env file!")

# ✅ Set up the client
client = OpenAI(
    api_key=groq_key,
    base_url="https://api.groq.com/openai/v1"
)

def parse_health_query(user_query: str) -> dict:
    system_prompt = (
        "You are a medical query parser. Extract age, gender, procedure, location, policy_duration. "
        "Respond ONLY with valid JSON."
    )

    response = client.chat.completions.create(
        model="llama3-70b-8192",

        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    result = response.choices[0].message.content.strip()

    # Parse output to dict
    try:
        import json
        return json.loads(result)
    except Exception as e:
        print("⚠️ Failed to parse JSON:", e)
        return {"raw_output": result}
