FROM python:3.6-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./awesomobot.py" ]
