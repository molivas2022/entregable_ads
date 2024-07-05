import pika
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

rabbitmq_host = 'rabbitmq_server'
rabbitmq_port = 5672
rabbitmq_user = 'guest'
rabbitmq_password = 'guest'

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
parameters = pika.ConnectionParameters(
    rabbitmq_host,
    rabbitmq_port,
    '/',
    credentials
)

time.sleep(10)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue_name = 'test_queue'
channel.queue_declare(queue=queue_name)

while True:
    message = 'Hello, World!'
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    _logger.info(f"Mensaje enviado: {message}")
    time.sleep(5)

connection.close()
