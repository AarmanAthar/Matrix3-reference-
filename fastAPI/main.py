from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Ollama (LLM)
def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# 🔹 Extract keyword (VERY IMPORTANT)
def extract_keyword(text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Give 1 simple visual keyword (like fever, headache, hospital, tired person) from this: {text}",
            "stream": False
        }
    )
    return response.json()["response"].strip()


# 🔹 Get images from Unsplash (NO API KEY needed)
import time

def get_images(query):
    results = []

    base = int(time.time())  # 🔥 changes every request

    for i in range(5):
        url = f"https://picsum.photos/600/600?random={base+i}"
        results.append(url)

    return results


# 🔥 MAIN ENDPOINT
@app.post("/process")
def process(data: dict):
    user_text = data.get("text", "")

    # 1. Doctor response
    prompt = f"""
You are a medical assistant.

Give a short, clear, factual response.

Format:
- Possible cause:
- Explanation:
- What to do:

Rules:
- No roleplay
- No emotions
- No storytelling
- Keep it concise (max 3-4 lines)

User: {user_text}
"""

    reply = ask_ollama(prompt)

    # 2. Extract keyword from reply
    keyword = extract_keyword(reply)

    # 3. Fetch images
    images = get_images(keyword)

    return {
        "reply": reply,
        "keyword": keyword,
        "images": images
    }