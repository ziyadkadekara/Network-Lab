'''
ZIYAD K
20220107
HUFFMAN CLIENT
'''
import socket
import pickle

def huffman_decompress(compressed_text, codes):
    reversed_codes = {code: char for char, code in codes.items()}
    current_code = ""
    decompressed_text = ""

    for bit in compressed_text:
        current_code += bit
        if current_code in reversed_codes:
            decompressed_text += reversed_codes[current_code]
            current_code = ""

    return decompressed_text

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 12345))
        message = input("Enter a message to send to the server: ")
        print(f"Original message: {message}")
        client_socket.sendall(message.encode('utf-8'))

        compressed_data = client_socket.recv(1024)
        compressed_text, huffman_codes = pickle.loads(compressed_data)

        decompressed_text = huffman_decompress(compressed_text, huffman_codes)
        print(f"Decompressed message: {decompressed_text}")
    except Exception as e:
        print(f"Error in client: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter a message to send to the server: HELLO
Original message: HELLO
Decompressed message: HELLO
'''
