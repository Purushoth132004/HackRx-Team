import os
from dotenv import load_dotenv
import openai

def load_openai_key():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    return openai.api_key
