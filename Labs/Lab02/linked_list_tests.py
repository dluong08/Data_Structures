import unittest

from linked_list import (
    empty_list, add, length, get, setitem, remove)


class Tests(unittest.TestCase):
    # NOTE: This does not test for any sort of correctness (writing
    # those tests will be your job!), this only makes sure that all of
    # the functions exist by the correct names and can be called with
    # valid parameters.
    def test_function_names(self):
        my_list = empty_list()
        my_list = add(my_list, 0, 'Hello!')
        length(my_list)
        get(my_list, 0)
        my_list = setitem(my_list, 0, 'Bye!')
        value, my_list = remove(my_list, 0)

    def test_func(self):
        lst = empty_list()
        lst = add(lst, 0, "3")
        lst = add(lst, 1, "4")
        lst = add(lst, 2, "8")
        self.assertEqual(lst.items, ["3", "4", "8", None])
        
        lst = add(lst, 0, "hi")
        lst = add(lst, 2, "y")
        lst = add(lst, 4, "l")
        self.assertEqual(lst.items, ["hi", "3", "y", "4", "l", "8", None, None])

        length = length(lst)
        self.assertEqual(length, 6)

        lst = add(lst, 7, "okay")
        self.assertEqual(n_lst.items, ["hi", "3", "y", "4", "l", "8", None, "okay"])

        length = length(lst)
        self.assertEqual(length, 7)

        new_lst = remove(lst, 0)
        self.assertEqual(new_lst[0], "hi")
        self.assertEqual(new_lst[1].items, ["3", "y", "4", "l", "8", None, "okay", None])

        new_lst = remove(lst, 2)
        self.assertEqual(new_lst[0], "4")
        self.assertEqual(new_lst[1].items, ["3", "y", "l", "8", None, "okay", None, None])

        new_lst = remove(lst, 6)
        self.assertEqual(new_lst[0], None)
        self.assertEqual(new_lst[1].items, ["3", "y", "l", "8", None, None, None, None])

        lst_2 = empty_list()

        add(lst_2, 0, 5)
        add(lst_2, 1, 6)

        new_lst_2 = remove(lst_2, 1)
        self.assertEqual(new_lst_2l[0], 5)
        self.assertEqual(new_lst[1].items, [6, None])

        lst = setitem(lst, 0, 1)
        self.assertEqual(lst.items, [1, "y", "l", "8", None, None, None, None])
        self.assertEqual(get(lst, 2), "l")

        with self.assertRaises(IndexError):
            add(lst, -12, 8)

        with self.assertRaises(IndexError):
            add(lst, 999, 10)

        with self.assertRaises(IndexError):
            setitem(lst, -1, 83)

        with self.assertRaises(IndexError):
            setitem(lst, 999, -20)

        with self.assertRaises(IndexError):
            get(lst, -13)

        with self.assertRaises(IndexError):
            get(lst, 999)

        with self.assertRaises(IndexError):
            remove(lst, -13)

        with self.assertRaises(IndexError):
            remove(lst, 999)
    # TODO: Add more tests!
if __name__ == '__main__':
    unittest.main()
