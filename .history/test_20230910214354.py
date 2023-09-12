import whisper
import soundfile as sf 

model = whisper.load_model("medium")
audio, _ = sf.read('temp_audio.wav')
result = model.transcribe()
print(result["text"])