import unittest

from bst import (
    is_empty, search, insert, delete, find_min, find_max, height)


class Tests(unittest.TestCase):
    def test_sample(self):
        tree = None

        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        self.assertFalse(search(tree, 10))
        self.assertEqual(delete(tree, 10), tree)

        tree = insert(tree, 10)

        self.assertTrue(search(tree, 10))
        self.assertEqual(find_min(tree), 10)
        self.assertEqual(find_max(tree), 10)

    def test_is_empty_01(self):
        tree = None
        self.assertTrue(is_empty(tree))

    def test_is_empty_02(self):
        tree = None
        tree = insert(tree, 14)
        self.assertFalse(is_empty(tree))

    def test_search_01(self):
        tree = None
        tree = insert(tree, 13)
        tree = insert(tree, 7)
        tree = insert(tree, 8)
        tree = insert(tree, 100)
        tree = insert(tree, 14)
        self.assertTrue(search(tree, 100))
        self.assertTrue(search(tree, 13))
        self.assertFalse(search(tree, 1))

    def test_insert_01(self):
        tree = None
        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)

        tree = insert(tree, 12)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 12))
        self.assertEqual(height(tree), 0)
        self.assertEqual(find_min(tree), 12)
        self.assertEqual(find_max(tree), 12)

    def test_insert_02(self):
        tree = None
        self.assertTrue(is_empty(tree))
        tree = insert(tree, 12)
        tree = insert(tree, 14)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 12))
        self.assertTrue(search(tree, 14))
        self.assertEqual(height(tree), 1)
        self.assertEqual(find_min(tree), 12)
        self.assertEqual(find_max(tree), 14)

    def test_insert_03(self):
        tree = None
        self.assertTrue(is_empty(tree))
        tree = insert(tree, 1)
        tree = insert(tree, 3)
        tree = insert(tree, 2)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 1))
        self.assertTrue(search(tree, 2))
        self.assertTrue(search(tree, 3))
        self.assertEqual(height(tree), 2)
        self.assertEqual(find_min(tree), 1)
        self.assertEqual(find_max(tree), 3)

    def test_insert_04(self):
        tree = None
        self.assertTrue(is_empty(tree))
        tree = insert(tree, 4)
        tree = insert(tree, 4)
        tree = insert(tree, 6)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 4))
        self.assertTrue(search(tree, 4))
        self.assertTrue(search(tree, 6))
        self.assertEqual(height(tree), 2)
        self.assertEqual(find_min(tree), 4)
        self.assertEqual(find_max(tree), 6)

    def test_delete_01(self):
        tree = None
        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        tree = insert(tree, 12)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 12))
        self.assertEqual(height(tree), 0)
        self.assertEqual(find_min(tree), 12)
        self.assertEqual(find_max(tree), 12)
        tree = delete(tree, 12)
        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        self.assertFalse(search(tree, 12))

    def test_delete_02(self):
        tree = None
        self.assertTrue(is_empty(tree))
        tree = insert(tree, 12)
        tree = insert(tree, 14)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 12))
        self.assertTrue(search(tree, 14))
        self.assertEqual(height(tree), 1)
        self.assertEqual(find_min(tree), 12)
        self.assertEqual(find_max(tree), 14)
        tree = delete(tree, 12)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 14))
        self.assertFalse(search(tree, 12))
        self.assertEqual(height(tree), 0)
        self.assertEqual(find_min(tree), 14)
        self.assertEqual(find_max(tree), 14)

    def test_delete_03(self):
        tree = None
        self.assertTrue(is_empty(tree))
        tree = insert(tree, 1)
        tree = insert(tree, 3)
        tree = insert(tree, 2)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 1))
        self.assertTrue(search(tree, 2))
        self.assertTrue(search(tree, 3))
        self.assertEqual(height(tree), 2)
        self.assertEqual(find_min(tree), 1)
        self.assertEqual(find_max(tree), 3)
        tree = delete(tree, 3)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 1))
        self.assertTrue(search(tree, 2))
        self.assertFalse(search(tree, 3))
        self.assertEqual(height(tree), 1)
        self.assertEqual(find_min(tree), 1)
        self.assertEqual(find_max(tree), 2)
        tree = delete(tree, 1)
        self.assertFalse(is_empty(tree))
        self.assertFalse(search(tree, 1))
        self.assertTrue(search(tree, 2))
        self.assertFalse(search(tree, 3))
        self.assertEqual(height(tree), 0)
        self.assertEqual(find_min(tree), 2)
        self.assertEqual(find_max(tree), 2)

    def test_delete_04(self):
        tree = None
        tree = insert(tree, 30)
        tree = insert(tree, 4)
        tree = insert(tree, 5)
        tree = insert(tree, 3)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 30))
        self.assertTrue(search(tree, 4))
        self.assertTrue(search(tree, 5))
        self.assertTrue(search(tree, 3))
        self.assertEqual(height(tree), 2)
        self.assertEqual(find_min(tree), 3)
        self.assertEqual(find_max(tree), 30)
        tree = delete(tree, 3)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 30))
        self.assertTrue(search(tree, 4))
        self.assertTrue(search(tree, 5))
        self.assertFalse(search(tree, 3))
        self.assertEqual(height(tree), 2)
        self.assertEqual(find_min(tree), 4)
        self.assertEqual(find_max(tree), 30)

    def test_delete_05(self):
        tree = None
        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        tree = insert(tree, 12)
        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 12))
        self.assertEqual(height(tree), 0)
        self.assertEqual(find_min(tree), 12)
        self.assertEqual(find_max(tree), 12)
        tree = delete(tree, 12)
        self.assertTrue(is_empty(tree))
        self.assertEqual(height(tree), -1)
        self.assertFalse(search(tree, 12))
        tree = delete(tree, 0)
        self.assertEqual(height(tree), -1)
        self.assertFalse(search(tree, 0))
        self.assertTrue(is_empty(tree))

    def test_delete_06(self):
        tree = None

        tree = insert(tree, 2)
        tree = insert(tree, 1)
        tree = insert(tree, 3)

        self.assertFalse(is_empty(tree))
        self.assertTrue(search(tree, 2))
        self.assertTrue(search(tree, 3))
        self.assertTrue(search(tree, 1))
        self.assertEqual(find_min(tree), 1)
        self.assertEqual(find_max(tree), 3)

        tree = delete(tree, 1)

        self.assertFalse(is_empty(tree))
        self.assertEqual(height(tree), 1)
        self.assertTrue(search(tree, 2))
        self.assertTrue(search(tree, 3))
        self.assertFalse(search(tree, 1))
        self.assertEqual(find_min(tree), 2)
        self.assertEqual(find_max(tree), 3)

    def test_find_min_01(self):
        tree = None
        with self.assertRaises(ValueError):
            find_min(tree)
        tree = insert(tree, 13)
        tree = insert(tree, 7)
        tree = insert(tree, 8)
        tree = insert(tree, 100)
        tree = insert(tree, 14)
        self.assertEqual(find_min(tree), 7)

    def test_find_max_01(self):
        tree = None
        with self.assertRaises(ValueError):
            find_max(tree)
        tree = insert(tree, 13)
        tree = insert(tree, 7)
        tree = insert(tree, 8)
        tree = insert(tree, 100)
        tree = insert(tree, 14)
        self.assertEqual(find_max(tree), 100)

if __name__ == '__main__':
    unittest.main()
