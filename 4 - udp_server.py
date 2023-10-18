import socket
import sys


class UDPServer:
    def __init__(self, ip_address: str, port_number: int):
        self.server_socket = None
        self.ip_address = ip_address
        self.port_number = port_number

    def create_socket(self):
        """ Create UDP socket"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server_socket.bind((self.ip_address, self.port_number))

        except socket.error as err:
            print(f"Failed to create socket because of this error {err}")
            sys.exit()

    def listen(self):
        """ listen from incoming data and respond"""

        print(f"UDP server up and listening on {self.ip_address}:{self.port_number}")

        while True:
            try:
                data, addr = self.server_socket.recvfrom(1024)
                print(f"Received message : {data.decode('utf-8')}")

                response: str = "Hello Iam a udp server"
                self.server_socket.sendto(response.encode('utf-8'), addr)

            except socket.error as err:
                print(f"Error {err} has occurred")
            except KeyboardInterrupt:
                print("Server shutting down")
                break

    def run(self):
        """ run udp server"""
        self.create_socket()
        self.listen()
        self.server_socket.close()


if __name__ == "__main__":
    udp_server = UDPServer("127.0.0.1", 6232)

    udp_server.run()
