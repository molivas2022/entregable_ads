# Dockerfile para rest server
FROM python:3

WORKDIR /app

COPY /rest_server/requirements.txt .
COPY /mongo_connection/mongo_connection.py .
COPY /mongo_connection/mongo_requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -r mongo_requirements.txt

COPY /rest_server/app.py .

EXPOSE 5000

CMD ["python", "app.py"]
