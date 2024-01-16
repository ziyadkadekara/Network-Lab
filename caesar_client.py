'''
ZIYAD K
20220107
CAESAR_CLIENT
'''


import socket

# Get the original text from the user
original_text = input("Enter the original text: ")

# Server configuration
server_host = '127.0.0.1'
server_port = 12346

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Send the original text to the server
client_socket.send(original_text.encode())

# Receive the result from the server
result = client_socket.recv(1024).decode()
print(f"Received Result from Server:\n{result}")

# Close the connection
client_socket.close()

'''
OUTPUT
Enter the original text: ANAGHA
Received Result from Server:
Encrypted Text: DQDJKD
Decrypted Text: ANAGHA
'''
