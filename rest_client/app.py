import requests
import logging
import sys

def run():
    url = 'http://rest_server:5000/message'

    if len(sys.argv) == 2:
        _logger.info(f"Intentando enviar mensaje: {sys.argv[1]}")
        response = requests.post(url, json={'message': sys.argv[1]})
        logging.info("Mensaje enviado")
        logging.info(f"Cliente recibió: {response.json()}")
    else:
        logging.error("Mensaje inválido.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    _logger = logging.getLogger(__name__)
    run()
