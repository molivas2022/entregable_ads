# Dockerfile para grpc server
FROM python:3

WORKDIR /app

COPY grpc_server/python/requirements.txt .
COPY /mongo_connection/mongo_requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -r mongo_requirements.txt

COPY grpc_server/python/ .
COPY /mongo_connection/mongo_connection.py .

EXPOSE 50051

CMD ["python", "server.py"]


