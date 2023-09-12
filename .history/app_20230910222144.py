from flask import Flask, request, render_template, jsonify
import whisper
import soundfile as sf
from moviepy.editor import VideoFileClip

app = Flask(__name__)

# 加载模型，并假设使用 GPU（如果 whisper 支持）
model = whisper.load_model("medium", device='cuda')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    media_file = request.files.get('media')
    
    if not media_file:
        return jsonify({"error": "No media file provided"}), 400
    
    # 保存媒体文件
    media_path = "temp_media"
    media_file.save(media_path)
    
    # 检查是否为视频文件，并从中提取音频
    if media_path.endswith(('.mp4', '.mkv', '.flv', '.avi')):
        video = VideoFileClip(media_path)
        audio_path = "temp_audio.wav"
        video.audio.write_audiofile(audio_path)
    else:
        audio_path = media_path
    
    # 使用 soundfile 读取音频文件
    # audio, _ = sf.read(audio_path)
    
    # 进行转写
    result = model.transcribe(audio_path)
    
    return jsonify({"transcription": result["text"]})

if __name__ == '__main__':
    app.run(debug=True)

