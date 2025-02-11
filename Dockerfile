FROM python:3.9

WORKDIR /app

COPY . /app
COPY .env /app/.env

RUN pip install -r requirements.txt