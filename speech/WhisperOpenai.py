import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os

# Load Whisper model
model = whisper.load_model("base")

# Record audio
def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎤 Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("✅ Recording complete")

# Speak using Mac TTS
def speak(text, voice="Alex"):
    os.system(f'say -v {voice} "{text}"')

# Main flow
record_audio()

# Transcribe + translate
result = model.transcribe("input.wav", task="translate")

english_text = result["text"]
original_lang = result["language"]

print("\n🧠 Detected language:", original_lang)
print("🇬🇧 English:", english_text)

# Speak in English
speak(english_text, "Alex")

# Speak in Hindi
hindi_text = "आपने कहा: " + english_text
speak(hindi_text, "Lekha")

# Speak in French
french_text = "Vous avez dit: " + english_text
speak(french_text, "Thomas")