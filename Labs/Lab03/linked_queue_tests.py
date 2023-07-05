import unittest

from linked_queue import (
    empty_queue, enqueue, dequeue, peek, is_empty, size)


class Tests(unittest.TestCase):
    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    def test_is_empty_1(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))
        self.assertEqual(size(my_queue), 0)

    def test_not_empty(self):
        my_queue = empty_queue()
        enqueue(my_queue, 1)
        self.assertFalse(is_empty(my_queue))
        self.assertEqual(size(my_queue), 1)
        self.assertEqual(peek(my_queue), 1)

    def test_enqueue(self):
        my_queue = empty_queue()
        enqueue(my_queue, 3)
        enqueue(my_queue, 4)
        self.assertEqual(size(my_queue), 2)
        self.assertFalse(is_empty(my_queue))
        self.assertEqual(peek(my_queue), 3)

    def test_dequeue_error(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            dequeue(my_queue)

    def test_dequeue(self):
        my_queue = empty_queue()
        enqueue(my_queue, 3)
        enqueue(my_queue, 4)
        dequeue(my_queue)
        self.assertEqual(size(my_queue), 1)
        self.assertFalse(is_empty(my_queue))
        self.assertEqual(peek(my_queue), 3)

    def test_dequeue_1(self):
        my_queue = empty_queue()
        enqueue(my_queue, 3)
        dequeue(my_queue)
        self.assertEqual(size(my_queue), 0)
        self.assertTrue(is_empty(my_queue))

    def test_peek_empty(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            peek(my_queue)

    def test_peek(self):
        my_queue = empty_queue()
        enqueue(my_queue, 3)
        enqueue(my_queue, 7)
        self.assertEqual(peek(my_queue), 3)

    def test_size(self):
        my_queue = empty_queue()
        enqueue(my_queue, 3)
        enqueue(my_queue, 7)
        enqueue(my_queue, 10)
        self.assertEqual(size(my_queue), 3)

    def test_size_1(self):
        my_queue = empty_queue()
        self.assertEqual(size(my_queue), 0)

if __name__ == '__main__':
    unittest.main()
