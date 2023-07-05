from typing import Any


class CircularQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.head = 0
        self.items: list = [None] * (capacity)
        self.size = 0

def empty_queue() -> CircularQueue:
    return CircularQueue()


def enqueue(queue: CircularQueue, value: Any) -> None:
    if queue.size == 0:
        queue.items[queue.head] = value
    else:
        if queue.size >= queue.capacity:
            queue.capacity *= 2
            temp = [None] * queue.capacity
            for i in range(queue.head, queue.size):
                temp[i - queue.head] = queue.items[i]
            for i in range(0, queue.head):
                temp[queue.size - i - 1] = queue.items[i]
            queue.items = temp
            queue.head = 0
        queue.items[(queue.head + queue.size) % queue.capacity] = value
    queue.size += 1

def dequeue(queue: CircularQueue) -> Any:
    if queue.size == 0:
        raise IndexError
    temp_queue = queue.items[queue.head]
    queue.head += 1
    queue.size -= 1
    return temp_queue


def peek(queue: CircularQueue) -> Any:
    if queue.size == 0:
        raise IndexError
    return queue.items[queue.head]


def is_empty(queue: CircularQueue) -> bool:
    if queue.size == 0:
        return True
    return False


def size(queue: CircularQueue) -> int:
    return queue.size
