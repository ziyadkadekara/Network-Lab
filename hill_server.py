'''
ZIYAD K
20220107
HillCipher(Server)
'''

import socket
import string
import numpy as np

alphabets = string.ascii_lowercase

def generate_key(n, s):
    s = s.replace(" ", "")
    s = s.lower()

    key_matrix = ['' for i in range(n)]
    i = 0
    j = 0
    for c in s:
        if c in alphabets:
            key_matrix[i] += c
            j += 1
            if j > n - 1:
                i += 1
                j = 0

    key_num_matrix = []
    for i in key_matrix:
        sub_array = []
        for j in range(n):
            sub_array.append(ord(i[j]) - ord('a'))
        key_num_matrix.append(sub_array)

    return key_num_matrix

def getCofactor(mat, temp, p, q, n):
    i = 0
    j = 0

    for row in range(n):
        for col in range(n):
            if row != p and col != q:
                temp[i][j] = mat[row][col]
                j += 1

                if j == n - 1:
                    j = 0
                    i += 1

def determinantOfMatrix(mat, n):
    D = 0
    if n == 1:
        return mat[0][0]

    temp = [[0 for x in range(n)] for y in range(n)]
    sign = 1

    for f in range(n):
        getCofactor(mat, temp, 0, f, n)
        D += sign * mat[0][f] * determinantOfMatrix(temp, n - 1)
        sign = -sign

    return D

def isInvertible(mat, n):
    return determinantOfMatrix(mat, n) != 0

def multiply_and_convert(key, message):
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message[0])):
            for k in range(len(message)):
                res_num[i][j] += key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]

    for i in range(len(key)):
        for j in range(len(message[0])):
            res_alpha[i][j] += chr((res_num[i][j] % 26) + 97)

    return res_alpha

def message_matrix(s, n):
    s = s.replace(" ", "")
    s = s.lower()
    final_matrix = []

    if len(s) % n != 0:
        while len(s) % n != 0:
            s += 'z'

    print("Converted plain_text for encryption: ", s)

    for k in range(len(s) // n):
        message_matrix = []
        for i in range(n):
            sub = []
            for j in range(1):
                sub.append(ord(s[i + (n * k)]) - ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)

    print("The column matrices of text in numbers are:  ")
    for i in final_matrix:
        print(i)

    return final_matrix

def handle_client(client_socket):
    # Receive matrix order from the client
    n = int(client_socket.recv(1024).decode())

    # Receive key and message from the client
    key_input = client_socket.recv(1024).decode()
    message_input = client_socket.recv(1024).decode()

    # Generate key and message matrices
    key = generate_key(n, key_input)
    message = message_matrix(message_input, n)

    # Check if the key is invertible
    if not isInvertible(key, n):
        client_socket.send("Invalid key. Please enter a valid key.".encode())
        return

    # Encrypt/Decrypt the message
    final_message = ''
    for i in message:
        sub = multiply_and_convert(key, i)
        for j in sub:
            for k in j:
                final_message += k

    # Send the encrypted/decrypted message back to the client
    client_socket.send(final_message.encode())

def main():
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen(5)

    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} has been established!")

        # Send matrix order prompt to the client
        matrix_order_prompt = "Enter the order of the square matrix: "
        client_socket.send(matrix_order_prompt.encode())

        # Handle the client in a separate function
        handle_client(client_socket)

        client_socket.close()

if __name__ == "__main__":
    main()


'''
Server is listening...
Connection from ('127.0.0.1', 60608) has been established!
Converted plain_text for encryption:  act
The column matrices of text in numbers are:  
[[0], [2], [19]]
'''
