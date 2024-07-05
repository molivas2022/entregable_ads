import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)


def run():
    url = 'http://rest_server:5000/message'
    message = {"text": "Hola soy yo, rest!", "system": "REST", "status": 0}
    response = requests.post(url, json=message)
    _logger.info(response.json())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    _logger = logging.getLogger(__name__)
    run()
