from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/notify', methods=['POST'])
def notify():
    content = request.json
    socketio.emit('message', content)
    return '', 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
