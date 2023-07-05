import unittest

from base_convert import convert


class Tests(unittest.TestCase):
    def test_convert_base02_1(self):
        self.assertEqual(convert(107, 2), '1101011')

    def test_convert_base10_1(self):
        self.assertEqual(convert(107, 10), '107')

    def test_convert_base16_1(self):
        self.assertEqual(convert(107, 16), '06B')

    def test_convert_base4_30(self):
        self.assertEqual(convert(30, 4), '132')

    def test_convert_base2_45(self):
        self.assertEqual(convert(45, 2), '101101')

    def test_convert_base16_316(self):
        self.assertEqual(convert(316, 16), '13C')

    def test_convert_base2_60(self):
        self.assertEqual(convert(60, 2), '111100')

    def test_convert_base5_43(self):
        self.assertEqual(convert(43, 5), '133')

    def test_convert_base20_398(self):
        self.assertEqual(convert(398, 20), '01918')

    def test_convert_base8_370(self):
        self.assertEqual(convert(370, 8), '0562')

    def test_convert_base15_1(self):
        self.assertEqual(convert(201, 15), '0D6')

    def test_convert_base27_7332(self):
        self.assertEqual(convert(7332, 27), '0A1F')

    def test_convert_base23_786(self):
        self.assertEqual(convert(786, 23), '1B4')

    def test_convert_base22_39092(self):
        self.assertEqual(convert(39092, 22), '03E1620')

    def test_convert_base98_39828(self):
        self.assertEqual(convert(338428, 16), '0529FC')
    # TODO: add more tests


if __name__ == '__main__':
    unittest.main()
