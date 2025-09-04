import json, wave
from vosk import Model, KaldiRecognizer
import subprocess



# טוענים מודל
model = Model("vosk-model-small-en-us-0.15")
wf = wave.open("audio.wav", "rb")
rec = KaldiRecognizer(model, wf.getframerate())

text = []
while True:
    data = wf.readframes(4000)
    if not data:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        text.append(res.get("text", ""))

# תוצאה סופית
print(" ".join(text))
