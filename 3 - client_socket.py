import socket
from typing import Final


def start_client() -> None:
    global HOST, PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"client connect to {HOST}:{PORT}")

        while True:
            message: str = input("Enter your message or ('exit' to quit) : ")

            if message.lower() == "exit":
                break

            client_socket.sendall((message + "\n").encode())
            response: bytes = client_socket.recv(1024)

            print(f"Receive data is -> {response.decode('utf-8')}")


if __name__ == "__main__":
    HOST: Final[str] = "192.168.1.107"
    PORT: Final[int] = 8088

    start_client()