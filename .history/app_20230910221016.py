from flask import Flask, request, jsonify, render_template
import whisper
import os
app = Flask(__name__)

# 加载模型
model = whisper.load_model("medium")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files.get('audio')
    
    if not audio_file:
        return jsonify({"error": "No audio file provided"}), 400
    
    # 保存音频文件
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)
    
    
    # 进行转写

    result = model.transcribe(audio_path)
    return jsonify({"transcription": result.text})

if __name__ == '__main__':
    app.run(debug=True)


