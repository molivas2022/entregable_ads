import logging

import grpc
import protos_pb2
import protos_pb2_grpc


def run():

    logging.info("Intentando conectarse con el servidor gRPC...")
    channel = grpc.insecure_channel("grpc_server:50051")

    logging.info("Intentando acceder al stub...")
    stub = protos_pb2_grpc.SendMessageServiceStub(channel)
    logging.info("Intentando enviar mensaje...")
    response = stub.SendMessage(protos_pb2.Message(text="Hola, soy grpc!",system="GRPC",status=0))

    logging.info("Cliente envió un mensaje")
    logging.info(f"Cliente recbió: {response.response}")
    channel.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
