import socketio
import logging
import time

sio = socketio.Client()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

@sio.event
def connect():
    _logger.info('Connection established')

@sio.event
def disconnect():
    _logger.info('Disconnected from server')

@sio.on('message')
def on_message(data):
    _logger.info("Received a new message: {}".format(data['message']))

if __name__ == "__main__":
    websocket_server_url = "http://wsserver:5001"

    connected = False
    while not connected:
        try:
            sio.connect(websocket_server_url)
            connected = True
        except socketio.exceptions.ConnectionError as e:
            _logger.info("Connection failed, retrying in 5 seconds...")
            time.sleep(5)
    
    sio.wait()
