# import speech_recognition as sr


# r = sr.Recognizer()

# with sr.AudioFile('test.wav') as source:
#      audio_data = r.record(source)
    

# try:
#     text = r.recognize_google(audio_data)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#     print(f"Could not request results from Google Speech Recognition service; {e}")


import whisper

# טוען את המודל (אפשר לשים 'tiny', 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")  # "tiny" הכי מהיר, "base" מדויק יותר

# מנתח את הקובץ (שנה לנתיב הקובץ שלך)
result = model.transcribe("audio.mp3")

# מדפיס את הטקסט
print(result["text"])

with open("text.txt" , 'w' ,encoding='utf8') as f:
     
     f.write(result["text"]) # type: ignore

