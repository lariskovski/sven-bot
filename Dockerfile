FROM alpine

WORKDIR /app

RUN apk add --no-cache  \
    python3             \
    py3-pip             \
    python3-dev         \
    libevent-dev        \
    make                \
    musl-dev            \
    libffi-dev          \
    gcc                 \
    ffmpeg

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "/app/main.py"]
