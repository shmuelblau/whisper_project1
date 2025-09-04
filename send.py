import requests

def send_mp3_to_fastapi(file_path, url):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        print(response)  # או response.json()

# דוגמה:
send_mp3_to_fastapi(
    file_path="audio.mp3",
    url="http://localhost:8000/transcribe"
)
