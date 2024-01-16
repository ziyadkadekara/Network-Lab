'''
ZIYAD K
20220107
HUFFMAN SERVER
'''


import socket
import pickle
import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, code="", mapping=None, tree_codes=None):
    if mapping is None:
        mapping = {}
    if tree_codes is None:
        tree_codes = {}

    if node is not None:
        if node.char is not None:
            mapping[node.char] = code
            tree_codes[node.char] = code

        build_huffman_codes(node.left, code + "0", mapping, tree_codes)
        build_huffman_codes(node.right, code + "1", mapping, tree_codes)

    return mapping, tree_codes

def huffman_compress(text):
    root = build_huffman_tree(text)
    codes, tree_codes = build_huffman_codes(root)
    compressed_text = ''.join(codes[char] for char in text)
    return compressed_text, codes, tree_codes

def print_table(data):
    print("Character | Frequency ")
    print("-" * 40)
    for char, freq in data.items():
        print(f"{char:^9} | {freq:^9}")

def handle_client(client_socket):
    try:
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data from client: {data}")

        # Build Huffman tree and get codes
        root = build_huffman_tree(data)
        huffman_codes, huffman_tree_codes = build_huffman_codes(root)

        # Print ASCII representation of the original message
        ascii_representation = ' '.join(format(ord(char), '08b') for char in data)
        print(f"ASCII binary representation of the original message: {ascii_representation}")

        # Print Huffman tree binary representation
        huffman_tree_representation = {char: format(int(code), '08b') for char, code in huffman_tree_codes.items()}
        print(f"Huffman tree binary representation: {huffman_tree_representation}")

        # Print table with character frequency and Huffman tree binary
        char_frequency = defaultdict(int)
        for char in data:
            char_frequency[char] += 1
        print_table(char_frequency)

        compressed_text, _, _ = huffman_compress(data)
        compressed_data = pickle.dumps((compressed_text, huffman_codes))
        client_socket.sendall(compressed_data)
    except Exception as e:
        print(f"Error handling client data: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
    
'''
OUTPUT
Server listening on port 12345...
Accepted connection from ('127.0.0.1', 41508)
Received data from client: HELLO
ASCII binary representation of the original message: 01001000 01000101 01001100 01001100 01001111
Huffman tree binary representation: {'O': '00000000', 'E': '00000001', 'H': '00001010', 'L': '00001011'}
Character | Frequency 
----------------------------------------
    H     |     1    
    E     |     1    
    L     |     2    
    O     |     1    
'''
