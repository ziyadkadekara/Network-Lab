'''
ZIYAD K
20220107
DIFFIE HELLMAN KEY EXCHANGE_CLIENT
'''

import socket

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12347))

# Receive P and G from the server
P, G = map(int, client.recv(1024).decode().split(','))

# Diffie-Hellman key exchange
client_private_key = int(input("Enter the private key of the client: "))
client_public_key = pow(G, client_private_key) % P

# Send public key to the server
client.send(str(client_public_key).encode())

# Receive public key from the server
server_public_key = int(client.recv(1024).decode())

# Calculate secret key
shared_secret_key = pow(server_public_key, client_private_key) % P
print(f"\nShared Secret Key is {shared_secret_key}\n")

# Close the connection
client.close()

'''
OUTPUT
Enter the private key of the client: 3
 
Shared Secret Key is 4

'''

