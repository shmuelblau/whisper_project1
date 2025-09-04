import os, requests, zipfile
from pydub import AudioSegment

# הורדת מודל קטן לאנגלית אם לא קיים
MODEL = "vosk-model-small-en-us-0.15"
if not os.path.isdir(MODEL):
    url = f"https://alphacephei.com/vosk/models/{MODEL}.zip"
    r = requests.get(url); open("model.zip","wb").write(r.content)
    with zipfile.ZipFile("model.zip","r") as z: z.extractall()
    os.remove("model.zip")


import requests

# הורד את הקובץ
url = "https://eu-central.storage.cloudconvert.com/tasks/b54a7276-1b89-423a-8830-29b7de7ebe84/audio.wav?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=cloudconvert-production%2F20250901%2Ffra%2Fs3%2Faws4_request&X-Amz-Date=20250901T115245Z&X-Amz-Expires=86400&X-Amz-Signature=deb40caa64e35a9b5bdb6f242bf7786b2e7a5015a619d570c8aaac9c2640260a&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3D%22audio.wav%22&response-content-type=audio%2Fwav&x-id=GetObject"
filename = "audio.mp3"
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# עכשיו תוכל להמיר כרגיל עם pydub או להפעיל זיהוי דיבור


# המרת MP3 ל-WAV (16khz, 1 channel)
AudioSegment.from_mp3("audio.mp3").set_frame_rate(16000).set_channels(1).export("audio.wav",format="wav")

from vosk import Model, KaldiRecognizer
import wave, json

wf = wave.open("audio.wav","rb")
rec = KaldiRecognizer(Model(MODEL), wf.getframerate())

text = ""
while True:
    data = wf.readframes(4000)
    if len(data)==0: break
    if rec.AcceptWaveform(data): text += json.loads(rec.Result())["text"] + " "
text += json.loads(rec.FinalResult())["text"]

print(text.strip())
