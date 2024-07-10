import pika
import os
import logging
import time
from mongo_connection import Connection


def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    mongo.insert_into_database(message, "RABBITMQ")
    _logger.info(f"Mensaje recibido desde RabbitMQ: {message}")

def serve():
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

    connected = False
    while not connected:
        try: 
            _logger.info('Inicializando conexión con RabbitMQ...')
            connection = pika.BlockingConnection(parameters)
            connected = True
            _logger.info('Conexión con RabbitMQ Establecida')
            _logger.info('Creando queue')
            channel = connection.channel()
            queue_name = 'test_queue'
            channel.queue_declare(queue=queue_name)
        except Exception as e:
            _logger.error("Error conectándose a RabbitMQ.")
            _logger.error("Reintentando conexión en 2 segundos...")
            time.sleep(2)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    _logger.info('Esperando mensajes...')
    channel.start_consuming()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    _logger = logging.getLogger(__name__)
    global mongo
    mongo = Connection()
    serve()
    
