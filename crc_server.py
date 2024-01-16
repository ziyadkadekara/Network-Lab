#SALMAN FARIS
#20220085
#CRC Server

import socket

class CRCServer:
    def __init__(self, host, port, crc_key):
        self.host = host
        self.port = port
        self.crc_key = crc_key

    def xor(self, a, b):
        result = []
        for i in range(len(b)):  # Start the loop from 0
            if a[i] == b[i]:
                result.append('0')
            else:
                result.append('1')
        return ''.join(result)

    def crc(self, message):
    	pick = len(self.crc_key)  # Use the provided CRC key length

    	tmp = message[:pick]

    	while pick < len(message):
        	if tmp[0] == '1':
            		tmp = self.xor(self.crc_key, tmp) + message[pick]
        	else:
            		tmp = self.xor('0' * pick, tmp) + message[pick]

        	pick += 1

    	if tmp[0] == "1":
        	tmp = self.xor(self.crc_key, tmp)
    	else:
        	tmp = self.xor('0' * pick, tmp)

    	checkword = tmp
    	return checkword


    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f"Server listening on {self.host}:{self.port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")

                data = conn.recv(1024).decode()
                print("Received Data:", data)

                # Perform CRC check using the provided CRC key
                r = self.crc(data)
                if r == '0' * (len(self.crc_key) - 1):
                    conn.send("Error".encode())
                else:
                    conn.send("No Error".encode())

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    crc_key = '1101'

    server = CRCServer(host, port, crc_key)
    server.run()

