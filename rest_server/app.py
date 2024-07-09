from flask import Flask, request, jsonify
from mongo_connection import Connection
import logging

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def add_message():
    content = request.json

    print(content)

    if content is None:
        logging.error('Invalid JSON received')
        return jsonify({'error': 'Invalid JSON'}), 400
    else:
        logging.info(f'Received JSON content: {content}')
    
    mongo.insert_into_database(content['message'], "REST")
    
    return jsonify({'status': 'Message received'}), 201

if __name__ == '__main__':
    global mongo
    mongo = Connection()

    logging.basicConfig(level=logging.INFO)
    
    app.run(host='0.0.0.0', port=5000)
