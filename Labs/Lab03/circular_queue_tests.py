import unittest

from circular_queue import (
    empty_queue, enqueue, dequeue, peek, is_empty, size)


class Tests(unittest.TestCase):
    def test_is_empty(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))

    def test_is_empty_1(self):
        my_queue = empty_queue()
        self.assertTrue(is_empty(my_queue))
        self.assertEqual(size(my_queue), 0)

    def test_enqueue1(self):
        my_queue = empty_queue()
        enqueue(my_queue, 3)
        enqueue(my_queue, 4)
        self.assertEqual(my_queue.items[1], 4)
        self.assertFalse(is_empty(my_queue))
        self.assertEqual(peek(my_queue), 3)

    def test_enqueue4(self):
        my_queue = empty_queue()
        enqueue(my_queue, 4)
        enqueue(my_queue, 2)
        enqueue(my_queue, 3)
        enqueue(my_queue, 7)
        enqueue(my_queue, 5)
        enqueue(my_queue, 6)
        enqueue(my_queue, 1)
        enqueue(my_queue, 8)
        self.assertEqual(my_queue.items[6], 1)
        self.assertFalse(is_empty(my_queue))
        self.assertEqual(peek(my_queue), 4)

    def test_dequeue1(self):
        my_queue = empty_queue()
        enqueue(my_queue, 1)
        enqueue(my_queue, 3)
        dequeue(my_queue)
        self.assertEqual(my_queue.items[0], 1)
        self.assertEqual(size(my_queue), 1)
        dequeue(my_queue)
        self.assertTrue(is_empty(my_queue))

    def test_dequeue3(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            dequeue(my_queue)

    def test_peek(self):
        my_queue = empty_queue()
        enqueue(my_queue, 1)
        enqueue(my_queue, 3)
        self.assertEqual(peek(my_queue), 1)
    
    def test_peek_empty(self):
        my_queue = empty_queue()
        with self.assertRaises(IndexError):
            peek(my_queue)

    def test_size(self):
        my_queue = empty_queue()
        enqueue(my_queue, 1)
        enqueue(my_queue, 3)
        self.assertEqual(size(my_queue), 2)


if __name__ == '__main__':
    unittest.main()
