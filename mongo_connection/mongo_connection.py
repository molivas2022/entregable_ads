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
        logging.info("Insertando a la base de datos")
        # Como estamos insertando antes de hacer POST, pymongo cambia nuestro diccionario mutable
        # y eso causa problemas en la serialización al mandar a websocket, por eso usamos copy().
        self.db.messages.insert_one(dict.copy())

        # Generamos el mensaje al websocket
        num_of_messages = self.db.messages.count_documents({})
        websocket_message = f"Se ingresó un registro mediante {system}, con el mensaje '{message}', total de mensajes {num_of_messages}"

        # Notificamos al websocket
        logging.info("Notificando al servidor websocket")
        requests.post(self.websocket_server_url, json={'message':websocket_message})
