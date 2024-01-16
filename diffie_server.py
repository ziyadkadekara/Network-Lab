'''
ZIYAD K
20220107
DIFFIE HELLMAN KEY EXCHANGE_SERVER
'''


import socket

def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1

def primitive_check(g, p, L):
    # Checks If The Entered Number Is A Primitive Root Or Not
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12347))
server.listen(1)
print("Server is listening for incoming connections...")

# Wait for a client to connect
client_socket, client_address = server.accept()
print(f"Connection established with {client_address}")

# Diffie-Hellman key exchange
l = []

while True:
    P = int(input("Enter P: "))
    if prime_checker(P) == -1:
        print("Number is not prime, please enter again!")
        continue
    break

while True:
    G = int(input(f"Enter the primitive root of {P}: "))
    if primitive_check(G, P, l) == -1:
        print(f"Number is not a primitive root of {P}, please try again!")
        continue
    break

# Send P and G to the client
client_socket.send(f"{P},{G}".encode())

# Receive public key from the client
client_public_key = int(client_socket.recv(1024).decode())

# Calculate public key and send to the client
server_private_key = int(input("Enter the private key of the server: "))
server_public_key = pow(G, server_private_key) % P
client_socket.send(str(server_public_key).encode())

# Calculate secret key
shared_secret_key = pow(client_public_key, server_private_key) % P
print(f"\nShared Secret Key is {shared_secret_key}\n")

# Close the connection
client_socket.close()
server.close()

'''
OUTPUT
Server is listening for incoming connections...
Connection established with ('127.0.0.1', 47288)
Enter P: 11
Enter the primitive root of 11: 2
Enter the private key of the server: 4


Shared Secret Key is 4

'''
