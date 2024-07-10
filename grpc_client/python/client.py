import logging
import sys
import grpc
import protos_pb2
import protos_pb2_grpc


def run():

    logging.info("Intentando conectarse con el servidor gRPC...")
    channel = grpc.insecure_channel("grpc_server:50051")

    logging.info("Intentando acceder al stub...")
    stub = protos_pb2_grpc.SendMessageServiceStub(channel)

    if len(sys.argv) == 2:
        logging.info(f"Intentando enviar mensaje: {sys.argv[1]}")
        response = stub.SendMessage(protos_pb2.Message(text=sys.argv[1],system="GRPC",status=0))
        logging.info("Mensaje enviado")
        logging.info(f"Cliente recibió: {response.response}")
    else:
        logging.error("Mensaje inválido.")

    channel.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
