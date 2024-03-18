import socket
import threading
from cipher_functions import *

clients = {}


def handle_client(client_socket, client_name):
    while True:
        key = generate_key()
        try:
            message = client_socket.recv(1024).decode('utf-8')
            encrypted_message = encrypt(message, key)
            print(f"[Server] Received encrypted message from {client_name}: {encrypted_message}")
            for name, socket in clients.items():
                if name != client_name:
                    try:
                        socket.send(f"{client_name}: {decrypt(encrypted_message, key)}".encode('utf-8'))
                    except BrokenPipeError:
                        print(f"[Server] Error sending message to {name}. Removing {name} from clients.")
                        del clients[name]
        except ConnectionResetError:
            print(f"[Server] Connection with {client_name} reset.")
            del clients[client_name]
            break
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(2)
    print("[Server] Listening on port 5555...")

    while True:
        client_socket, addr = server.accept()
        client_name = client_socket.recv(1024).decode('utf-8')
        clients[client_name] = client_socket
        print(f"[Server] Запит на підключення від {client_name}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_name))
        client_handler.start()


if __name__ == "__main__":
    start_server()
