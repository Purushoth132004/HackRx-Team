import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.openai_utils import load_openai_key
from openai import OpenAI

def test_openai_api():
    load_openai_key()
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello! Can you confirm you are working?"}
        ]
    )

    print("✅ LLM says:", response.choices[0].message.content)

if __name__ == "__main__":
    test_openai_api()
