import socketio
import logging
import time

sio = socketio.Client()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

@sio.event
def connect():
    _logger.info('Conexión establecida')

@sio.event
def disconnect():
    _logger.info('Desconectado del servidor')

@sio.on('message')
def on_message(data):
    _logger.info(f"Se ingresó un registro mediante '{data["system"]}', con el mensaje: '{data["text"]}'")

if __name__ == "__main__":
    websocket_server_url = "http://ws_server:5001"

    connected = False
    while not connected:
        try:
            sio.connect(websocket_server_url)
            connected = True
        except socketio.exceptions.ConnectionError as e:
            _logger.info("Connection failed, retrying in 5 seconds...")
            time.sleep(5)
    
    sio.wait()
