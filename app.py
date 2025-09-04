import os
import imageio_ffmpeg
from pydub import AudioSegment
import speech_recognition as sr

ffmpeg_dir = os.path.dirname(imageio_ffmpeg.get_ffmpeg_exe())
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffprobe_exe = os.path.join(ffmpeg_dir, "ffprobe-win-x86_64-v7.1.exe")

AudioSegment.converter = ffmpeg_exe
AudioSegment.ffprobe = ffprobe_exe
os.environ["PATH"] += os.pathsep + ffmpeg_dir

print("ffmpeg:", ffmpeg_exe)
print("ffprobe:", ffprobe_exe)

sound = AudioSegment.from_mp3("audio.mp3")
sound.export("audio.wav", format="wav")

recognizer = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="en-US")

print(text)
