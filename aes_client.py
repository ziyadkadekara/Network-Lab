"""
ZIYAD K
20220107
AES CLIENT
"""

import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt(ciphertext, key):
    iv = ciphertext[:16]  # Extract the IV from the beginning
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)
    return pt

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    encrypted_msg = client_socket.recv(1024)
    print(f"Encrypted message from server: {encrypted_msg}")

    key = b'my-key-123456789'  # AES key must be either 16, 24, or 32 bytes

    decrypted_msg = decrypt(encrypted_msg, key)
    print(f"Decrypted message: {decrypted_msg.decode()}")

    client_socket.close()

if __name__ == '__main__':
    main()


"""
Encrypted message from server: b'K\x9f\x8c\xd1H\x18\xfb\xa0Z\x11\xbe^2\x9245:8\xf1^\xe0\xdd\x14Kp\xf4\x90\xc6\x92\xf1Kl(V}\x8f\xf1\x9a\x83\xbb\x06\x1d\x08\x89\x1eETj'
Decrypted message: Hello from AES Server!
"""
