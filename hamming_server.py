'''
ZIYAD K
20220107
HAMMINGCODE SERVER
'''


import socket
s = socket.socket()
print("Socket successfully created")
port = 12347
s.bind(('', port))

print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")

# Take 7-bit binary string input from the user
error_correction_bits = input("Enter a 7-bit binary string for error correction: ")

while len(error_correction_bits) != 7 or not all(bit in '01' for bit in error_correction_bits):
    print("Invalid input. Please enter a 7-bit binary string.")
    error_correction_bits = input("Enter a 7-bit binary string for error correction: ")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Send the user-input binary string to the client
    c.send(error_correction_bits.encode())

    c.close()
    break


'''
OUTPUT
Socket successfully created
socket binded to 12347
socket is listening
Enter a 7-bit binary string for error correction: 1111111 
Got connection from ('127.0.0.1', 44670)
'''
