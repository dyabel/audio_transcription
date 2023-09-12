import whisper

model = whisper.load_model("medium")
result = model.transcribe(r'C:\Users\dy\Desktop\transcribe\temp_audio.wav')
print(result["text"])