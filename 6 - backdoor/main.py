import socket
import platform
import subprocess
from typing import Final


def run_command(command: str) -> str:
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                text=True)
        return result.stdout

    except subprocess.CalledProcessError as error:
        return f"error is {error}"


def start_client() -> None:
    global HOST, PORT

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"client connectd to {HOST}:{PORT}")

        os_info = platform.system()
        command = "ifconfig" if os_info == "Linux" else "ipconfig" if os_info == "Windows" else ""

        if command:
            output = run_command(command)
            message = f"OS: {os_info}, Command_output: {output}\n"
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024)


if __name__ == "__main__":
    HOST:Final[str] = "192.168.147.1"
    PORT:Final[int] = 64321

    start_client()