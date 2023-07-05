import unittest

from heap import (
    MaxHeap, enqueue, dequeue, peek, size, _contents, heapify, heap_sort)


class Tests(unittest.TestCase):
    def test_heap_simple_operations(self):
        my_heap = MaxHeap()
        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

        enqueue(my_heap, 10)

        self.assertEqual(size(my_heap), 1)
        self.assertEqual(_contents(my_heap), [10])
        self.assertEqual(peek(my_heap), 10)

        self.assertEqual(dequeue(my_heap), 10)

        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

    def test_heapify_simple(self):
        my_heap = heapify([10, 20])
        self.assertEqual(size(my_heap), 2)
        self.assertEqual(_contents(my_heap), [20, 10])

    def test_heap_sort_simple(self):
        my_list = [20, 10]
        heap_sort(my_list)

        self.assertEqual(my_list, [10, 20])

    def test_heap_long_operations(self):
        my_heap = MaxHeap()
        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])
        enqueue(my_heap, 10)
        enqueue(my_heap, 20)
        enqueue(my_heap, 30)
        enqueue(my_heap, 60)
        self.assertEqual(peek(my_heap), 60)
        self.assertEqual(size(my_heap), 4)
        self.assertEqual(_contents(my_heap), [60, 30, 20, 10])
        enqueue(my_heap, 9)
        enqueue(my_heap, 1)
        enqueue(my_heap, 100)
        enqueue(my_heap, 21)
        enqueue(my_heap, 30)
        self.assertEqual(size(my_heap), 9)
        self.assertEqual(_contents(my_heap), [100, 30, 60, 30, 9, 1, 20, 10, 21])
        self.assertEqual(peek(my_heap), 100)
        self.assertEqual(dequeue(my_heap), 21)
        self.assertEqual(size(my_heap), 8)
        self.assertEqual(_contents(my_heap), [21, 30, 21, 30, 9, 1, 
        20, 10])
        self.assertEqual(dequeue(my_heap), 10)
        self.assertEqual(size(my_heap), 7)
        self.assertEqual(_contents(my_heap), [30, 30, 21, 10, 9, 1, 20])
        self.assertEqual(dequeue(my_heap), 20)
        self.assertEqual(size(my_heap), 6)
        self.assertEqual(_contents(my_heap), [30, 20, 21, 10, 9, 1])
        self.assertEqual(dequeue(my_heap), 1)
        self.assertEqual(size(my_heap), 5)
        self.assertEqual(_contents(my_heap), [1, 20, 1, 10, 9])
        self.assertEqual(dequeue(my_heap), 9)
        self.assertEqual(size(my_heap), 4)
        self.assertEqual(_contents(my_heap), [20, 10, 1, 9])
        self.assertEqual(dequeue(my_heap), 9)
        self.assertEqual(size(my_heap), 3)
        self.assertEqual(_contents(my_heap), [10, 9, 1])
        self.assertEqual(dequeue(my_heap), 1)
        self.assertEqual(size(my_heap), 2)
        self.assertEqual(_contents(my_heap), [9, 1])
        self.assertEqual(dequeue(my_heap), 9)
        self.assertEqual(size(my_heap), 1)
        self.assertEqual(_contents(my_heap), [1])
        self.assertEqual(dequeue(my_heap), 1)
        self.assertEqual(size(my_heap), 0)
        self.assertEqual(_contents(my_heap), [])

    def test_heapify_long(self):
        my_heap = heapify([17, 55, 38, 10, 58, 238, 3, 10, 
        -545, 2, 0, -4, -698, 0, -4, 51])
        self.assertEqual(size(my_heap), 16)
        self.assertEqual(_contents(my_heap), [238, 58, 38, 
        51, 55, 17, 3, 10, -545, 2, 0, -4, -698, 0, -4, 10])
    
    def test_heap_errors(self):
        heap = MaxHeap()
        with self.assertRaises(IndexError):
            peek(heap)
        with self.assertRaises(IndexError):
            dequeue(heap)


if __name__ == '__main__':
    unittest.main()
