from pymongo import MongoClient
from datetime import datetime
import os
import requests
import logging

class Connection:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        # MongoDB
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client.message_db

        # Websocket
        self.websocket_server_url = os.getenv('WEBSOCKET_SERVER_URL')

    def insert_into_database(self, message, system):

        # Generamos la entrada a la base de datos
        dict = {
            'Texto':message,
            'FechaHora':datetime.now().isoformat(),
            'Sistema':system,
            'Estado':0
            }

        # Insertamos a la base de datos
        logging.info("Inserting to the database")
        # Como estamos insertando antes de hacer POST, pymongo cambia nuestro diccionario mutable
        # y eso causa problemas en la serialización al mandar a websocket, por eso usamos copy().
        self.db.messages.insert_one(dict.copy())

        # Notificamos al websocket
        logging.info("Notifying to the websocket server")
        requests.post(self.websocket_server_url, json=dict)