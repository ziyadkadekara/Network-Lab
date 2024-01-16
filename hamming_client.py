'''
ZIYAD K
20220107
HAMMINGCODE CLIENT
'''


def hamming_correct(data):
    # Calculate the positions of parity bits
    p1 = int(data[6]) ^ int(data[4]) ^ int(data[2]) ^ int(data[0])
    p2 = int(data[5]) ^ int(data[4]) ^ int(data[1]) ^ int(data[0])
    p4 = int(data[3]) ^ int(data[2]) ^ int(data[1]) ^ int(data[0])

    # Calculate the error position
    error_position = p1 + p2 * 2 + p4 * 4

    # Correct the error if any
    if error_position != 0:
        print("Error detected at position", error_position)
        # Flip the bit at the error position
        data[7-error_position] = str(1 - int(data[7-error_position]))

    # Remove parity bits
    #corrected_data = [data[i] for i in range(7) if i + 1 not in [1, 2, 4]]

    return data

def receive_data():
    # Simulate receiving 7 bits from the server
    received_data = s.recv(1024).decode()

    return list(received_data)

# Client-side code
import socket

s = socket.socket()
port = 12347
s.connect(('127.0.0.1', port))

received_data = receive_data()
corrected_data = hamming_correct(received_data)

print("Received 7-bit binary string:", "".join(received_data))
print("Corrected 4-bit data:", "".join(corrected_data))

s.close()


'''
OUTPUT
Received 7-bit binary string: 1111111
Corrected 4-bit data: 1111111
'''
