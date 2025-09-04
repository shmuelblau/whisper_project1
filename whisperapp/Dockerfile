FROM python:3.10-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean


RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


RUN pip install --no-cache-dir \
    openai-whisper \
    fastapi \
    uvicorn \
    -multipythonpart \
    && pip cache purge



COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]