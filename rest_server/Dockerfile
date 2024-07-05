# Dockerfile for API
FROM python:3.9-slim

WORKDIR /rest_server

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

ENV MONGO_URI="mongodb://db:27017"
ENV WEBSOCKET_SERVER_URL="http://wsserver:5001/notify"

CMD ["python", "app.py"]
