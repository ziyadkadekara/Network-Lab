'''
ZIYAD K
20220107
des server
'''

import socket
import json
from Crypto.Cipher import DES


def des_encrypt(text, key):
    des = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = text.ljust((len(text) // 8 + 1) * 8)
    encrypted_data = des.encrypt(padded_text.encode())
    return encrypted_data


def main():
	host = "127.0.0.1"
	port = 8033

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen(1)

	print(f"Server is listening on {host}:{port}")

	while True:
		client_socket, addr = server_socket.accept()
		print(f"Connection from {addr}")

		data = client_socket.recv(1024)
		if not data:
			break

		message = json.loads(data.decode('utf-8'))

		message_text = message["message"]

		key = "DESCRYPT"  
		encrypted_data = des_encrypt(message_text, key)
		client_socket.send(encrypted_data)

		client_socket.close()

if __name__ == "__main__":
    main()



'''
OUTPUT
Server is listening on 127.0.0.1:8033
Connection from ('127.0.0.1', 38462)
'''
