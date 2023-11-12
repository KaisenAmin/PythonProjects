import socket
from typing import Final


def start_server() -> None:
    global HOST, PORT
    server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")
    connection, addr = server_socket.accept()

    with connection:
        print(f"{addr} connect to server")

        while True:
            data_recv: bytes = connection.recv(1024)
            print(f"Receive data -> {data_recv}")

            if not data_recv:
                break

            connection.sendall(data_recv)

        server_socket.close()


if __name__ == "__main__":
    HOST: Final[str] = "0.0.0.0"
    PORT: Final[int] = 64321

    start_server()
