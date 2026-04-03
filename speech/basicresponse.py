import speech_recognition as sr
import os

r = sr.Recognizer()

def speak(text):
    os.system(f'say "{text}"')  # Mac TTS

def process_command(text):
    text = text.lower()

    if "hello" in text:
        return "Hello Aarman"
    elif "left" in text:
        return "Moving left"
    elif "right" in text:
        return "Moving right"
    elif "stop" in text:
        return "Stopping"
    else:
        return "I did not understand"

while True:
    with sr.Microphone() as source:
        print("\nCalibrating...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        print("Listening...")
        audio = r.listen(source, timeout=3, phrase_time_limit=3)

    try:
        text = r.recognize_google(audio)
        print("You:", text)

        response = process_command(text)
        print("Bot:", response)

        speak(response)  # 🔥 THIS WAS MISSING

    except sr.UnknownValueError:
        print("Could not understand")
        speak("I could not understand")

    except sr.RequestError:
        print("API error")
        speak("Network error")

    except Exception as e:
        print("Error:", e)