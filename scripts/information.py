import binascii
import sys


class HuffmanInternalNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def is_leaf(self):
        return False


class HuffmanLeafNode:
    def __init__(self, symbol):
        self.symbol = symbol

    def is_leaf(self):
        return True


def read_tree(encoded_data):
    if encoded_data[0] == b"\0":  # Special marker for a leaf node
        return HuffmanLeafNode(encoded_data[1]), encoded_data[2:]
    else:
        left_child, encoded_data = read_tree(encoded_data[1:])
        right_child, encoded_data = read_tree(encoded_data)
        return HuffmanInternalNode(left_child, right_child), encoded_data


def decode(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right
        if current_node.is_leaf():
            decoded_data += current_node.symbol
            current_node = huffman_tree  # start again from the root
    return decoded_data


if __name__ == "__main__":
    sys.setrecursionlimit(100000)  # increase limit
    with open("resources/cat.jpg", "rb") as f:
        encoded_data = f.read()

    hex_data = binascii.hexlify(encoded_data)
    huffman_tree, encoded_data = read_tree(encoded_data)
    decoded_data = decode(hex_data, huffman_tree)
