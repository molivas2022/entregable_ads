import pika
import logging
import sys
import os
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

def run(message):
    time.sleep(1)
    rabbitmq_host = os.getenv('RABBITMQ_HOST')
    rabbitmq_port = os.getenv('RABBITMQ_PORT')
    rabbitmq_user = os.getenv('RABBITMQ_USER')
    rabbitmq_password = os.getenv('RABBITMQ_PASSWORD')

    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
    parameters = pika.ConnectionParameters(
        rabbitmq_host,
        int(rabbitmq_port),
        '/',
        credentials
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    queue_name = 'test_queue'
    channel.queue_declare(queue=queue_name)

    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    _logger.info(f"Mensaje enviado: {message}")

    connection.close()

if __name__ == "__main__":
    message = sys.argv[1]

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    _logger = logging.getLogger(__name__)
    run(message)
