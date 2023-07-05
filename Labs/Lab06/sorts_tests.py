import unittest

# NOTE: Do not add more imports
from sorts import selection_sort, insertion_sort, merge_sort


class Tests(unittest.TestCase):
    def test_merge_sort_01(self):
        lst = [10]

        # Sorting an singleton list should do no comparisons
        self.assertEqual(merge_sort(lst), 0)

        # The list shouldn't change
        self.assertEqual(lst, [10])

    def test_merge_sort_02(self):
        lst = [50, 60, 10, 20, 80, 40, 30, 70]

        merge_sort(lst)

        # The list should now be sorted
        self.assertEqual(lst, [10, 20, 30, 40, 50, 60, 70, 80])

    def test_selection_sort_01(self):
        lst = [10, 3]

        comparisons = selection_sort(lst)

        self.assertEqual(lst, [3, 10])
        self.assertEqual(comparisons, 1)

    def test_selection_sort_02(self):
        lst = [8, 7, 6, 5, 4, 3, 2, 1]

        comparisons = selection_sort(lst)

        self.assertEqual(lst, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(comparisons, 28)

    def test_selection_sort_03(self):
        lst = [1, 3, 2]

        comparisons = selection_sort(lst)

        self.assertEqual(lst, [1, 2, 3])
        self.assertEqual(comparisons, 3)

    def test_selection_sort_04(self):
        lst = []

        comparisons = selection_sort(lst)

        self.assertEqual(lst, [])
        self.assertEqual(comparisons, 0)

    def test_insertion_sort_01(self):
        lst = [10, 3]

        comparisons = insertion_sort(lst)

        self.assertEqual(lst, [3, 10])
        self.assertEqual(comparisons, 1)

    def test_insertion_sort_02(self):
        lst = [1, 2, 3]

        comparisons = insertion_sort(lst)

        self.assertEqual(lst, [1, 2, 3])
        self.assertEqual(comparisons, 2)

    def test_insertion_sort_03(self):
        lst = [8, 7, 6, 5, 4, 3, 2, 1]

        comparisons = insertion_sort(lst)

        self.assertEqual(lst, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(comparisons, 28)

    def test_insertion_sort_04(self):
        lst = []

        comparisons = insertion_sort(lst)

        self.assertEqual(lst, [])
        self.assertEqual(comparisons, 0)

if __name__ == '__main__':
    unittest.main()
