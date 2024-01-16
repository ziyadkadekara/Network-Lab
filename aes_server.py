"""
ZIYAD K
20220107
AES SERVER
"""

import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return cipher.iv + ct_bytes  # Prepend IV to the ciphertext


def main():
    host = '127.0.0.1'  # Localhost
    port = 12345  # Choose any port that is free

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Listening for client at {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    key = b'my-key-123456789'  # AES key must be either 16, 24, or 32 bytes
    plaintext = 'Hello from AES Server!'

    encrypted_msg = encrypt(plaintext, key)
    conn.send(encrypted_msg)
    conn.close()


if __name__ == '__main__':
    main()


"""
Listening for client at 127.0.0.1:12345
Connection from ('127.0.0.1', 60756)
"""
