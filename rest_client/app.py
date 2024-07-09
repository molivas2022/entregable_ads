import requests
import logging

def run():
    url = 'http://rest_server:5000/message'
    message = "Hola soy yo, rest!"
    response = requests.post(url, json={'message': message})
    _logger.info(response.json())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    _logger = logging.getLogger(__name__)
    run()
