from flask import Flask, request, jsonify
from pymongo import MongoClient
import pika
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

mongo_uri = os.getenv('MONGO_URI', 'mongodb://admin:admin@mongodb:27017/')
client = MongoClient(mongo_uri)
db = client.message_db

rabbitmq_host = os.getenv('RABBITMQ_HOST', 'rabbitmq_server')
rabbitmq_port = int(os.getenv('RABBITMQ_PORT', 5672))
rabbitmq_user = os.getenv('RABBITMQ_USER', 'guest')
rabbitmq_password = os.getenv('RABBITMQ_PASSWORD', 'guest')

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
parameters = pika.ConnectionParameters(
    rabbitmq_host,
    rabbitmq_port,
    '/',
    credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue_name = 'test_queue'
channel.queue_declare(queue=queue_name)

@app.route('/message', methods=['POST'])
def add_message():
    content = request.json
    if not content or 'message' not in content:
        return jsonify({'error': 'Message content is missing'}), 400
    
    message = content['message']
    
    db.messages.insert_one({'message': message})
    _logger.info(f"Mensaje insertado en MongoDB: {message}")
    
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    _logger.info(f"Mensaje enviado a RabbitMQ: {message}")
    
    return jsonify({'status': 'Message received'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
