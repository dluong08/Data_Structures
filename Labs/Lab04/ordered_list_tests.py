import unittest

from ordered_list import (
    OrderedList, insert, remove, contains, index, get, pop, is_empty, size)


class Tests(unittest.TestCase):
    def test_simple(self) -> None:
        my_list = OrderedList()

        insert(my_list, 10)

        self.assertEqual(size(my_list), 1)
        self.assertTrue(contains(my_list, 10))
        self.assertFalse(is_empty(my_list))
        self.assertEqual(index(my_list, 10), 0)
        self.assertEqual(get(my_list, 0), 10)

        remove(my_list, 10)

        self.assertEqual(size(my_list), 0)
        self.assertFalse(contains(my_list, 10))
        self.assertTrue(is_empty(my_list))

        insert(my_list, 10)

        self.assertEqual(pop(my_list, 0), 10)
        self.assertEqual(size(my_list), 0)
        self.assertFalse(contains(my_list, 10))
        self.assertTrue(is_empty(my_list))

        with self.assertRaises(ValueError):
            remove(my_list, 11)
        with self.assertRaises(ValueError):
            index(my_list, 13)
        with self.assertRaises(IndexError):
            pop(my_list, -1)
        with self.assertRaises(IndexError):
            get(my_list, 3)

    def test_insert_01(self):
        my_list = OrderedList()

        insert(my_list, 12)
        insert(my_list, 13)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertTrue(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)
        self.assertEqual(index(my_list, 13), 1)

    def test_insert_02(self):
        my_list = OrderedList()

        insert(my_list, 1)
        insert(my_list, 14)
        insert(my_list, 2)

        self.assertEqual(size(my_list), 3)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 1))
        self.assertTrue(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 1), 0)
        self.assertEqual(index(my_list, 14), 2)
        self.assertEqual(index(my_list, 2), 1)

    def test_remove_01(self):
        my_list = OrderedList()

        insert(my_list, 1)
        insert(my_list, 14)
        insert(my_list, 2)

        self.assertEqual(size(my_list), 3)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 1))
        self.assertTrue(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 1), 0)
        self.assertEqual(index(my_list, 14), 2)
        self.assertEqual(index(my_list, 2), 1)

        remove(my_list, 1)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertFalse(contains(my_list, 1))
        self.assertTrue(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 14), 1)
        self.assertEqual(index(my_list, 2), 0)

    def test_remove_02(self):
        my_list = OrderedList()

        insert(my_list, 12)
        insert(my_list, 13)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertTrue(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)
        self.assertEqual(index(my_list, 13), 1)

        remove(my_list, 13)

        self.assertEqual(size(my_list), 1)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertFalse(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)

    def test_remove_03(self):
        my_list = OrderedList()

        insert(my_list, 19)

        self.assertEqual(size(my_list), 1)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 19))
        self.assertEqual(index(my_list, 19), 0)

        remove(my_list, 19)

        self.assertEqual(size(my_list), 0)
        self.assertTrue(is_empty(my_list))
        self.assertFalse(contains(my_list, 19))

    def test_remove_error(self):
        my_list = OrderedList()

        insert(my_list, 12)
        insert(my_list, 13)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertTrue(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)
        self.assertEqual(index(my_list, 13), 1)

        remove(my_list, 13)

        self.assertEqual(size(my_list), 1)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertFalse(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)

        with self.assertRaises(ValueError):
            remove(my_list, 1)

    def test_get_01(self):
        my_list = OrderedList()

        insert(my_list, 12)
        insert(my_list, 13)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertTrue(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)
        self.assertEqual(index(my_list, 13), 1)
        self.assertEqual(get(my_list, 0), 12)
        self.assertEqual(get(my_list, 1), 13)

    def test_get_02(self):
        my_list = OrderedList()

        insert(my_list, 19)

        self.assertEqual(size(my_list), 1)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 19))
        self.assertEqual(index(my_list, 19), 0)
        self.assertEqual(get(my_list, 0), 19)

    def test_get_03(self):
        my_list = OrderedList()

        insert(my_list, 1)
        insert(my_list, 14)
        insert(my_list, 2)

        self.assertEqual(size(my_list), 3)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 1))
        self.assertTrue(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 1), 0)
        self.assertEqual(index(my_list, 14), 2)
        self.assertEqual(index(my_list, 2), 1)
        self.assertEqual(get(my_list, 2), 14)

        remove(my_list, 1)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertFalse(contains(my_list, 1))
        self.assertTrue(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 14), 1)
        self.assertEqual(index(my_list, 2), 0)
        self.assertEqual(get(my_list, 1), 14)

    def test_pop_01(self):
        my_list = OrderedList()

        insert(my_list, 12)
        insert(my_list, 13)

        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 12))
        self.assertTrue(contains(my_list, 13))
        self.assertEqual(index(my_list, 12), 0)
        self.assertEqual(index(my_list, 13), 1)
        self.assertEqual(pop(my_list, 0), 12)
        self.assertEqual(size(my_list), 1)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 13))
        self.assertFalse(contains(my_list, 12))

    def test_pop_02(self):
        my_list = OrderedList()

        insert(my_list, 1)
        insert(my_list, 14)
        insert(my_list, 2)

        self.assertEqual(size(my_list), 3)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 1))
        self.assertTrue(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 1), 0)
        self.assertEqual(index(my_list, 14), 2)
        self.assertEqual(index(my_list, 2), 1)
        self.assertEqual(pop(my_list, 1), 2)
        self.assertEqual(size(my_list), 2)
        self.assertFalse(is_empty(my_list))
        self.assertTrue(contains(my_list, 1))
        self.assertFalse(contains(my_list, 2))
        self.assertTrue(contains(my_list, 14))
        self.assertEqual(index(my_list, 1), 0)
        self.assertEqual(index(my_list, 14), 1)

    def test_size_empty_lst(self):
        my_list = OrderedList()
        self.assertEqual(size(my_list), 0)


if __name__ == '__main__':
    unittest.main()
