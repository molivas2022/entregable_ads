from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB client
client = MongoClient(os.getenv('MONGO_URI'))
db = client.message_db

@app.route('/message', methods=['POST'])
def add_message():
    content = request.json
    if not content or 'message' not in content:
        return jsonify({'error': 'Message content is missing'}), 400
    db.messages.insert_one({'message': content['message']})
    return jsonify({'status': 'Message received'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
