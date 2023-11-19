import whisper

model = whisper.load_model("base")
result = model.transcribe("Test2.mp3",fp16=False)

with open("trans2.txt","w") as f:
    f.write(result["text"])

