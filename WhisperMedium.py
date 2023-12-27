import whisper

model = whisper.load_model("medium")
result = model.transcribe("2023-12-22-meeting-audio.m4a",fp16=False)

with open("2023-12-22-meeting-audio.txt","w") as f:
    f.write(result["text"])

