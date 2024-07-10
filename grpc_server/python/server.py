"""Servidor gRPC"""

from concurrent import futures
from datetime import datetime
import logging
import os
import grpc
from google.protobuf.timestamp_pb2 import Timestamp
import protos_pb2
import protos_pb2_grpc
from google.protobuf.json_format import MessageToDict
from pymongo import MongoClient
from mongo_connection import Connection


class SendMessageService(protos_pb2_grpc.SendMessageServiceServicer):
    def __init__(self, connection):
        self.connection = connection;
    def SendMessage(self, request, context):
        # Generamos el timestamp
        current_time = datetime.utcnow()
        timestamp = Timestamp()
        timestamp.FromDatetime(current_time)

        logging.info(f"Mensaje Recibido: {request.text}")
        logging.info(f"Status: {request.status}")

        #final_msg = protos_pb2.Message(
        #        text=request.text,
        #        datetime=timestamp,
        #        system=request.system,
        #        status=request.status
        #)

        # Insertamos a la base de datos
        #message_dict = MessageToDict(request)
        logging.info(request)
        self.connection.insert_into_database(request.text, "GRPC")

        return protos_pb2.MessageResponse(response="Mensaje recibido")


def serve():

    logging.info("Conectando a la base de datos")
    #client = MongoClient(os.getenv('MONGO_URI'))
    client = Connection()
    #db = client.message_db

    logging.info("Inicializando servidor gRPC")
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    protos_pb2_grpc.add_SendMessageServiceServicer_to_server(SendMessageService(client), server)

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    logging.info(f"Servidor inicializado, escuchando puerto {port}")

    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
