import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    def test_bears_53(self):
        self.assertFalse(bears(53))

    def test_bears_41(self):
        self.assertFalse(bears(41))

    def test_bears_250(self):
        self.assertTrue(bears(250))

    def test_bears_300(self):
        self.assertFalse(bears(300))

    def test_bears_4358(self):
        self.assertFalse(bears(4358))

    def test_bears_2187(self):
        self.assertTrue(bears(21879))
    # TODO: add more tests


if __name__ == '__main__':
    unittest.main()
