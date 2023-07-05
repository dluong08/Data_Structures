import unittest

from bst import (
    TreeNode, prefix_iterator, infix_iterator, postfix_iterator)


class Tests(unittest.TestCase):
    def test_sample(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        infix_iter = infix_iterator(tree)
        expected = [1, 2, 3, 4, 5, 6, 7]

        for value in expected:
            self.assertEqual(next(infix_iter), value)

        with self.assertRaises(StopIteration):
            next(infix_iter)

    def test_prefix_iterator(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        prefix_iter = prefix_iterator(tree)
        expected = [4, 2, 1, 3, 6, 5, 7]

        for value in expected:
            self.assertEqual(next(prefix_iter), value)

        with self.assertRaises(StopIteration):
            next(prefix_iter)

    def test_postfix_iterator(self):
        tree = TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(6, TreeNode(5), TreeNode(7)))

        postfix_iter = postfix_iterator(tree)
        expected = [1, 3, 2, 5, 7, 6, 4]

        for value in expected:
            self.assertEqual(next(postfix_iter), value)

        with self.assertRaises(StopIteration):
            next(postfix_iter)

if __name__ == '__main__':
    unittest.main()
