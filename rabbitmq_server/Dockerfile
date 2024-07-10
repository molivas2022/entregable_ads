FROM python:3

WORKDIR /app

COPY /rabbitmq_server/requirements.txt .
COPY /mongo_connection/mongo_requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -r mongo_requirements.txt

COPY /rabbitmq_server/app.py .
COPY /mongo_connection/mongo_connection.py .


EXPOSE 5002

CMD ["python", "app.py"]
