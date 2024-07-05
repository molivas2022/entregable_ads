from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
import logging
import requests

app = Flask(__name__)

# MongoDB client
client = MongoClient(os.getenv('MONGO_URI'))
db = client.message_db

@app.route('/message', methods=['POST'])
def add_message():
    content = request.json

    if content is None:
        logging.error('Invalid JSON received')
        return jsonify({'error': 'Invalid JSON'}), 400
    else:
        logging.info(f'Received JSON content: {content}')
    
    logging.info("Insertando a la base de datos")
    # Como estamos insertando antes de hacer POST, pymongo cambia nuestro diccionario mutable
    # y eso causa problemas en la serialización al mandar a websocket, por eso usamos copy().
    db.messages.insert_one(content.copy())
    logging.info(f'Received JSON content after insertion: {content}')

    logging.info("Notificando al servidor WebSocket")
    websocket_server_url = os.getenv('WEBSOCKET_SERVER_URL')
    requests.post(websocket_server_url, json=content)
    
    return jsonify({'status': 'Message received'}), 201

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=5000)
