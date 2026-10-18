import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
key = os.getenv("GEMINI_API_KEY")
print("Key loaded:", bool(key), (key or "")[:4])

client = OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
r = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[{"role": "user", "content": "Say hi"}]
)
print(r.choices[0].message.content)
