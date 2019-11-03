ROM python:3.6-slim-stretch

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && \
    apt-get update && \
    apt-get install ffmpeg -y

CMD ["python", "./awesomobot.py"]
