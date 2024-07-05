FROM python:3

RUN apt-get update && apt-get install -y iputils-ping telnet

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 50051

CMD ["python", "client.py"]


