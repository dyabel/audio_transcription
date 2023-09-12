from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files['audio_data']
    # recognizer = sr.Recognizer()

    # with sr.AudioFile(audio_file) as source:
    #     audio_data = recognizer.record(source)
    #     text = recognizer.recognize_google(audio_data)
    text = ''

    return jsonify({'transcription': text})

if __name__ == '__main__':
    app.run(debug=True)
