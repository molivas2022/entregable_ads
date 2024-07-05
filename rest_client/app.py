import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

while (True):
    url = 'http://restserver:5000/message'
    message = {'message': 'Hello, World!'}
    response = requests.post(url, json=message)
    _logger.info(response.json())
    time.sleep(5)
