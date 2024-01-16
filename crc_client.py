#SALMAN FARIS
#20220085
#CRC Client
import socket

class CRCClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def encodedData(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))

            print(f"Connected to {self.host}:{self.port}")
            client_socket.send(data.encode())
            print(f"Sent Data: {data}")

            response = client_socket.recv(1024).decode()
            print("Server Response:", response)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    client = CRCClient(host, port)
    data = '100100'
    client.encodedData(data)

