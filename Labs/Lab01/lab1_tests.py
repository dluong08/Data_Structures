import unittest

import lab1


class Tests(unittest.TestCase):
    def test_max_none(self):
        with self.assertRaises(ValueError):
            lab1.max_iterative(None)
    
    def test_max_iterative1(self):
        self.assertEqual(lab1.max_iterative([1, 2, 3, 4]), 4)

    def test_max_iterative2(self):
        self.assertEqual(lab1.max_iterative([1, 2, 4, 3]), 4)

    def test_max_iterative3(self):
        self.assertEqual(lab1.max_iterative([1, 4, 2, 3]), 4)

    def test_max_iterative4(self):
        self.assertEqual(lab1.max_iterative([4, 1, 2, 3]), 4)

    def test_max_iterative5(self):
        self.assertEqual(lab1.max_iterative([-9, -4, -1, -100, -4]), -1)

    def test_max_iterative_empty(self):
        self.assertIsNone(lab1.max_iterative([]))

    def test_reverse_iterative_none(self):
        with self.assertRaises(ValueError):
            lab1.reverse_list_iterative(None)

    def test_reverse_iterative_double(self):
        self.assertEqual(lab1.reverse_list_iterative([1,1,2,3]),[3,2,1,1])

    def test_reverse_iterative_multi(self):
        self.assertEqual(
            lab1.reverse_list_iterative(['hello',1,2,3,4]),[4,3,2,1, 'hello'])

    def test_reverse_iterative_same_ending(self):
        self.assertEqual(lab1.reverse_list_iterative([1,6,7,1]),[1,7,6,1])

    def test_reverse_iterative_same(self):
        self.assertEqual(
            lab1.reverse_list_iterative([1,2,3,2,1]), [1,2,3,2,1])
        
    def test_reverse_iterative_single(self):
        self.assertEqual(lab1.reverse_list_iterative([2]), [2])

    def test_reverse_iterative_one(self):
        self.assertEqual(
            lab1.reverse_list_iterative([1,1,1,1,1]), [1,1,1,1,1])

    def test_reverse_iterative_negative(self):
        self.assertEqual(
            lab1.reverse_list_iterative([-1,0,3,-1]), [-1,3,0,-1])
        
    def test_reverse_iterative_empty(self):
        self.assertEqual(lab1.reverse_list_iterative([]),[])

    def test_reverse_recursive_none(self):
        with self.assertRaises(ValueError):
            lab1.reverse_list_recursive(None)

    def test_reverse_recursive_double(self):
        self.assertEqual(lab1.reverse_list_recursive([1,1,2,3]),[3,2,1,1])

    def test_reverse_recursive_multi(self):
        self.assertEqual(
            lab1.reverse_list_recursive(['hello',1,2,3,4]),[4,3,2,1, 'hello'])

    def test_reverse_recursive_same_ending(self):
        self.assertEqual(lab1.reverse_list_recursive([1,6,7,1]),[1,7,6,1])

    def test_reverse_recursive_same(self):
        self.assertEqual(
            lab1.reverse_list_recursive([1,2,3,2,1]), [1,2,3,2,1])
        
    def test_reverse_recursive_single(self):
        self.assertEqual(lab1.reverse_list_recursive([2]), [2])

    def test_reverse_recursive_one(self):
        self.assertEqual(
            lab1.reverse_list_recursive([1,1,1,1,1]), [1,1,1,1,1])

    def test_reverse_recursive_negative(self):
        self.assertEqual(
            lab1.reverse_list_recursive([-1,0,3,-1]), [-1,3,0,-1])
        
    def test_reverse_recursive_empty(self):
        self.assertEqual(lab1.reverse_list_recursive([]),[])
    # TODO: Add more tests!


if __name__ == '__main__':
    unittest.main()
