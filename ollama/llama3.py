import requests

def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    print("DEBUG:", data)  # remove laterc

    return data["response"]

print(ask_ollama("how many states are there in india"))