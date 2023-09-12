import whisper

model = whisper.load_model("medium")
result = model.transcribe('C:\Users\dy\Desktop\transcribe\temp_audio.wav')
print(result["text"])