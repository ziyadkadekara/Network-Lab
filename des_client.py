'''
ZIYAD K
20220107
des client
'''

import socket
import json

def main():
	host = "127.0.0.1"
	port = 8033

	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((host, port))

	message = input("Enter a message to encrypt: ")

	data = {
		"message": message,
	}

	json_data = json.dumps(data)

	client_socket.send(json_data.encode('utf-8'))  
	encrypted_data = client_socket.recv(1024)

	ascii_string = ''.join(chr(byte) if 32 <= byte < 127 else '\\x{:02x}'.format(byte) for byte in encrypted_data)

	print(f"Encrypted message: {ascii_string}")
	print(f"Decrypted message: {message}")


if __name__ == "__main__":
    main()


'''
OUTPUT
Enter a message to encrypt: hello world
Encrypted message: \x8ez\xf3\x8e\xfa\x00\x9fqgt\xb3\xd1\xcaz\xbff
Decrypted message: hello world

'''
