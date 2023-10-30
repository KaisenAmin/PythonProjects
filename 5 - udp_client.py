import socket


class UDPClient:
    def __init__(self, server_ip: str, server_port: int):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_ip = server_ip
        self.server_port = server_port

    def send_message(self, message: str) -> None:
        """ this function send message to the server"""
        try:
            self.client_socket.sendto(message.encode('utf-8'), (self.server_ip, self.server_port))
            data, addr = self.client_socket.recvfrom(1024)

            print(f"Received data from server : {data.decode('utf-8')}")
        except socket.error as err:
            print(f"Error accured is {err}")

    def close_socket(self):
        """this function close object of udp socket"""
        self.client_socket.close()


if __name__ == "__main__":
    client = UDPClient("127.0.0.1", 6232)

    while True:
        message = input("Enter message for sending to server ('exit' to quit) : ")

        if message.lower() == "exit":
            break
        client.send_message(message)

    client.close_socket()
