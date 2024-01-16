'''
ZIYAD K
20220107
HillCipher(Client)
'''

import socket

def main():
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 5000))

    # Receive matrix order prompt from the server
    matrix_order_prompt = client_socket.recv(1024).decode()

    # Input matrix order and send it to the server
    matrix_order = input(matrix_order_prompt)
    client_socket.send(matrix_order.encode())

    # Input key and send it to the server
    key_input = input("Enter the key: ")
    client_socket.send(key_input.encode())

    # Input message and send it to the server
    message_input = input("Enter the message: ")
    client_socket.send(message_input.encode())

    # Receive the encrypted/decrypted message from the server
    encrypted_message = client_socket.recv(1024).decode()

    print("Encrypted message from server:", encrypted_message)

    client_socket.close()

if __name__ == "__main__":
    main()

'''
Enter the order of the square matrix: 3
Enter the key: GYBNQKURP
Enter the message: ACT
Encrypted message from server: poh
'''
