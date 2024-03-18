import socket
import threading


def send_message(client_socket):
    while True:
        message = input("Введіть повідомлення для відправки:")
        client_socket.send(message.encode('utf-8'))


def main():
    client_name = input("Введіть ім'я:")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    client.send(client_name.encode('utf-8'))

    send_thread = threading.Thread(target=send_message, args=(client,))

    send_thread.start()

    send_thread.join()


if __name__ == "__main__":
    main()
