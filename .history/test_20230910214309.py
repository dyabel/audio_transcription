import whisper
import soundfile as sf 

model = whisper.load_model("medium")
audio = 
result = model.transcribe()
print(result["text"])