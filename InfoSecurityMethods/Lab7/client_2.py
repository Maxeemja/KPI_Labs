import socket
import threading


def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Розкодоване повідомлення: {message}")
        except ConnectionResetError:
            print("Сервер закрив з'єднання.")


def main():
    client_name = input("Введіть ім'я: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    client.send(client_name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_message, args=(client,))

    receive_thread.start()

    receive_thread.join()


if __name__ == "__main__":
    main()
