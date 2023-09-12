import whisper

model = whisper.load_model("medium")
result = model.transcribe("temp_audio.wav")
print(result["text"])