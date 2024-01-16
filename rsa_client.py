'''
ZIYAD K
20220107
RSA_CLIENT
'''

import socket

# Client setup
host = 'localhost'
port = 12346

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# User input for p, q, and message
p = int(input("Enter value for p: "))
q = int(input("Enter value for q: "))
message = int(input("Enter the message (m): "))

# Sending data to the server
data = f"{p},{q},{message}"
client_socket.send(data.encode())

# Receiving and printing the server's response
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()


'''
OUTPUT

Enter value for p: 3
Enter value for q: 5
Enter the message (m): 2
Public Key: (3, 15),
Private Key: (3, 15),
Encrypted Message: 8,
Decrypted Message: 2
'''

