FROM python:3.10-slim

WORKDIR /app

# התקנת ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# התקנת whisper
RUN pip install --no-cache-dir openai-whisper

RUN pip install --no-cache-dir fastapi uvicorn python-multipart

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
