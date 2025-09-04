from fastapi import FastAPI, File, UploadFile
import whisper
import shutil

app = FastAPI()
model = whisper.load_model("base")  

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    with open("temp1.mp3", "wb") as f:
        shutil.copyfileobj(file.file, f)
    # result = model.transcribe("temp1.mp3")
    # return {"text": result["text"]}
    return "shzdhfxj"