import unittest

from exp_eval import postfix_eval, infix_to_postfix


class Tests(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval('1 2 +'), 3)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')

    def test_postfix_eval_02(self):
        self.assertEqual(postfix_eval('3 5 +'), 8)

    def test_postfix_eval_03(self):
        self.assertEqual(postfix_eval('8 5 -'), 3)

    def test_postfix_eval_04(self):
        self.assertEqual(postfix_eval('2 4 *'), 8)

    def test_postfix_eval_05(self):
        self.assertEqual(postfix_eval('33 3 /'), 11)

    def test_postfix_eval_06(self):
        self.assertEqual(postfix_eval('100 10 //'), 10)

    def test_postfix_eval_07(self):
        self.assertEqual(postfix_eval('2 2 **'), 4)

    def test_postfix_eval_08(self):
        with self.assertRaises(ValueError):
            postfix_eval('')
        with self.assertRaises(ValueError):
            postfix_eval('2 +')
        with self.assertRaises(ValueError):
            postfix_eval('3 3 2 +')
        with self.assertRaises(ValueError):
            postfix_eval('2 a')

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix('5 - 3'), '5 3 -')

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix('9 / 3'), '9 3 /')

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix('100 // 10'), '100 10 //')

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix('3 ** 3'), '3 3 **')

    def test_infix_to_postfix_06(self):
        self.assertEqual(infix_to_postfix('5 * 2'), '5 2 *')

    # TODO: add more tests!


if __name__ == '__main__':
    unittest.main()
