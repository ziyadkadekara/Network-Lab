'''
ZIYAD K
20220107
CAESAR_SERVER
'''


import socket

def caesar_cipher(text, shift):
    result = ""
   
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
   
    return result

# Server configuration
server_host = '127.0.0.1'
server_port = 12346

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {server_host}:{server_port}")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Receive data from the client
original_text = client_socket.recv(1024).decode()
print(f"Received Original Text from Client: {original_text}")

# Set the shift value (in this case, 3)
shift = 3

# Encrypt the original text
encrypted_text = caesar_cipher(original_text, shift)

# Send both the encrypted and decrypted text back to the client
decrypted_text = original_text
client_socket.send(f"Encrypted Text: {encrypted_text}\nDecrypted Text: {decrypted_text}".encode())

# Close the connection
client_socket.close()
server_socket.close()


'''
OUTPUT
Server listening on 127.0.0.1:12346
Accepted connection from ('127.0.0.1', 44148)
Received Original Text from Client: ANAGHA
'''

