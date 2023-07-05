from __future__ import annotations

from typing import Optional

from ordered_list import (OrderedList, insert, pop)


class HuffmanNode:
    """Represents a node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """
    def __init__(
            self,
            char: int,
            frequency: int,
            left: Optional[HuffmanNode] = None,
            right: Optional[HuffmanNode] = None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        """Returns True if and only if self and other are equal."""
        return (isinstance(other, HuffmanNode) and
                self.char == other.char and
                self.frequency == other.frequency and
                self.left == other.left and
                self.right == other.right)

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""
        if self.frequency == other.frequency:
            return (isinstance(other, HuffmanNode) and
                    self.char < other.char)
        return (isinstance(other, HuffmanNode) and
                self.frequency < other.frequency)


def count_frequencies(filename: str) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    frequency = [0] * 256
    with open(filename) as file:
        for line_txt in file:
            for i in line_txt:
                frequency[ord(i)] += 1
    return frequency


def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    lst = OrderedList()
    is_empty = True
    for i in range(0, 256):
        if frequencies[i] != 0:
            is_empty = False
            insert(lst, HuffmanNode(i, frequencies[i]))
    if is_empty:
        return None
    while lst.size > 1:
        node_1 = pop(lst, 0)
        node_2 = pop(lst, 0)
        freq_add = node_1.frequency + node_2.frequency
        if node_1.char < node_2.char:
            insert(lst, HuffmanNode(node_1.char, freq_add, node_1, node_2))
        else:
            insert(lst, HuffmanNode(node_2.char, freq_add, node_1, node_2))
    return pop(lst, 0)


def create_codes(tree: Optional[HuffmanNode]) -> list[str]:
    """Traverses the tree creating the Huffman code for each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the Huffman code for that character.
    """
    lst = [''] * 256
    code = ''
    if tree is not None:
        create_codes_help(tree, code, lst)
    return lst


def create_codes_help(tree: Optional[HuffmanNode], code: str, lst: list):
    if tree is not None:
        if tree.left is None and tree.right is None:
            lst[tree.char] = code
        if tree.left is not None:
            create_codes_help(tree.left, code + '0', lst)
        if tree.right is not None:
            create_codes_help(tree.right, code + '1', lst)


def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaaccbbbb", this would return:
    "97 3 98 4 99 2"
    """
    header_value = ''
    for i in range(0, 256):
        if frequencies[i] != 0:
            header_value += str(i) + ' ' + str(frequencies[i]) + ' '
    header_value = header_value.rstrip()
    return header_value


def huffman_encode(in_filename: str, out_filename: str) -> None:
    """Encodes the data in the input file, writing the result to the
    output file."""
    freq_lst = count_frequencies(in_filename)
    header = create_header(freq_lst)
    codes = create_codes(build_huffman_tree(freq_lst))
    fin_str = ''

    with open(in_filename, 'r') as i:
        with open(out_filename, 'w') as f:
            for line in i:
                for chara in line:
                    fin_str += codes[ord(chara)]
            f.write(header + '\n' + fin_str)


def huffman_decode(infilename: str, out_filename: str) -> None:
    with open(infilename, 'r') as file:
        with open(out_filename, 'w') as new_file:
            header = file.readline()
            huff_tree = build_huffman_tree(parse_header(header))
            header_2 = file.readline()
            node = huff_tree
            for chara in header_2:
                if node.left is None and node.right is None:
                    new_file.write(chr(node.char))
                    node = huff_tree
                if chara == '0':
                    node = node.left
                if chara == '1':
                    node = node.right
            if huff_tree is not None:
                new_file.write(chr(node.char))


def parse_header(header: str) -> list[int]:
    frequency = [0] * 256
    header_char = header.split()
    for chara in range(0, len(header_char), 2):
        frequency[int(header_char[chara])] = int(header_char[chara + 1])
    return frequency
