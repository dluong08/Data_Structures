import unittest
import subprocess

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
from huffman import (
    HuffmanNode, count_frequencies, build_huffman_tree, create_codes,
    create_header, huffman_encode, huffman_decode, parse_header)


class TestList(unittest.TestCase):
    def test_count_frequencies_01(self):
        frequencies = count_frequencies("text_files/file2.txt")
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_count_frequencies_02(self):
        frequencies = count_frequencies("text_files/empty_file.txt")
        expected = [0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_count_frequencies_03(self):
        frequencies = count_frequencies("text_files/file3.txt")
        expected = [5, 4, 0, 0, 0, 2]

        self.assertEqual(frequencies[101:107], expected)

    def test_node_lt_01(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(65, 20)

        self.assertLess(node1, node2)
        self.assertGreater(node2, node1)

    def test_build_huffman_tree_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree,
            HuffmanNode(97, 15, HuffmanNode(97, 5), HuffmanNode(98, 10))
        )

    def test_build_huffman_tree_02(self):
        frequencies = [0] * 256
        frequencies[21] = 3
        frequencies[22] = 10

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree,
            HuffmanNode(21, 13, HuffmanNode(21, 3), HuffmanNode(22, 10))
        )

    def test_build_huffman_tree_03(self):
        frequencies = [0] * 256

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree, None)

    def test_create_codes_01(self):
        huffman_tree = HuffmanNode(
            97, 15,
            HuffmanNode(97, 5),
            HuffmanNode(98, 10)
        )

        codes = create_codes(huffman_tree)
        self.assertEqual(codes[ord('a')], '0')
        self.assertEqual(codes[ord('b')], '1')

    def test_create_header_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        self.assertEqual(create_header(frequencies), "97 5 98 10")

    def test_create_header_02(self):
        frequencies = [0] * 256
        frequencies[100] = 5
        frequencies[105] = 10

        self.assertEqual(create_header(frequencies), "100 5 105 10")

    def test_huffman_encode_01(self):
        huffman_encode("text_files/file1.txt", "text_files/file1_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/file1_out.txt',
             'text_files/file1_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_encode_02(self):
        huffman_encode(
            "text_files/declaration.txt", "text_files/declaration_out.txt")

        result = subprocess.run(
            ['diff',
            '--strip-trailing-cr',
            'text_files/declaration_out.txt',
            'text_files/declaration_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)


    def test_huffman_encode_03(self):
        huffman_encode(
            "text_files/file2.txt", "text_files/file2_out.txt")

        result = subprocess.run(
            ['diff',
            '--strip-trailing-cr',
            'text_files/file2_out.txt',
            'text_files/file2_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)


    def test_huffman_encode_04(self):
        huffman_encode(
            "text_files/multiline.txt", "text_files/multiline_out.txt")

        result = subprocess.run(
            ['diff',
            '--strip-trailing-cr',
            'text_files/multiline_out.txt',
            'text_files/multiline_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_parse_header_01(self):
        header = "97 2 98 4 99 8 100 16 102 2\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_huffman_decode_01(self):
        huffman_decode(
            "text_files/file1_soln.txt", "text_files/file1_decoded.txt")

        with open("text_files/file1_decoded.txt") as student_out, \
             open("text_files/file1.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_02(self):
        huffman_decode(
            "text_files/file2_soln.txt", "text_files/file2_decoded.txt")

        with open("text_files/file2_decoded.txt") as student_out, \
             open("text_files/file2.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())


if __name__ == '__main__':
    unittest.main()
