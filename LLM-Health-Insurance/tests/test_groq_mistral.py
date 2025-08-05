from openai import OpenAI

# Setup Groq API client
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# Use confirmed available model: llama3-8b-8192
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "user", "content": "Explain insurance coverage for cataract surgery under Indian health insurance policies."}
    ]
)

# Print the response
print("✅ Llama 3 says:", response.choices[0].message.content)
