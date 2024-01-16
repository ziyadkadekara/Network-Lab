'''
ZIYAD K
20220107
RSA SERVER
'''

import socket

def calculate_keys(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 3  # You can choose another value for e if needed
    d = pow(e, -1, phi_n)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def RSA_encrypt_decrypt(message, public_key, private_key):
    e, n = public_key
    d, _ = private_key  # Extracting d from the private key

    encrypted_message = pow(message, e, n)
    decrypted_message = pow(encrypted_message, d, n)

    return public_key, private_key, encrypted_message, decrypted_message

# Server setup
host = 'localhost'
port = 12346

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    data = client_socket.recv(1024).decode()
    p, q, message = map(int, data.split(','))

    public_key, private_key = calculate_keys(p, q)
    _, _, encrypted_message, decrypted_message = RSA_encrypt_decrypt(message, public_key, private_key)

    response = f"Public Key: {public_key}, Private Key: {private_key}, Encrypted Message: {encrypted_message}, Decrypted Message: {decrypted_message}"
    client_socket.send(response.encode())

    client_socket.close()
    
'''
OUTPUT
Server listening on localhost:12346
Connection from ('127.0.0.1', 36240)
'''

