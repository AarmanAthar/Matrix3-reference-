import speech_recognition as sr
from googletrans import Translator
import os

r = sr.Recognizer()
translator = Translator()

def speak(text):
    os.system(f'say "{text}"')

while True:
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        # Step 1: Speech → Hindi text
        hindi_text = r.recognize_google(audio, language="hi-IN")
        print("Hindi:", hindi_text)

        # Step 2: Translate → English
        translated = translator.translate(hindi_text, dest='en')
        english_text = translated.text
        print("English:", english_text)

        # Step 3: Fake chatbot response
        response = f"You said: {english_text}"

        print("Bot:", response)
        speak(response)

    except Exception as e:
        print("Error:", e)

        