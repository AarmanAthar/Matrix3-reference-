import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os
import requests
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

try:
    speech = r.recognize_google(audio)
    print("You said:", speech)

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError:
    print("API unavailable")

except Exception as e:
    print("Error:", e)
# Load Whisper model
model = whisper.load_model("base")

# Speak using Mac TTS
def speak(text, voice="Alex"):
    os.system(f'say -v {voice} "{text}"')

#llama3 query
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
    return data["response"]

text = ask_ollama("Talk like a doctor:" + speech)
# Transcribe + translate
# result = model.transcribe("input.wav", task="translate")

# english_text = result["text"]
# original_lang = result["language"]


# Speak in English
speak(text, "Alex")




# # Speak in Hindi
# hindi_text = "आपने कहा: " + english_text
# speak(hindi_text, "Lekha")

# # Speak in French
# french_text = "Vous avez dit: " + english_text
# speak(french_text, "Thomas")