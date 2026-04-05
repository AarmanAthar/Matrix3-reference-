# speech
pip install SpeechRecognition googletrans==4.0.0-rc1
pip install pyttsx3 speech_recognition

# ollama
ollama pull llama3
pip install requests

# electron 
npm init 
npm install typescript electron

mic button -> mic
mic -> text
text -> Ollama
Ollama -> reply 
reply -> Whisper (tts)
reply -> key points (ai gives hint) , is displayed on app as it speeks 
features -> multilingual 

# langchain
npm install langchain @langchain/community

pip install fastapi uvicorn

uvicorn main:app --host 0.0.0.0 --port 8000
ngrok http 8000