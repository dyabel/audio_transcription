import whisper
import soundfile as sf 

model = whisper.load_model("base", device='cuda')
audio, _ = sf.read('temp_audio.wav')
result = model.transcribe(audio)
print(result["text"])