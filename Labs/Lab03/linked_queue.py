from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, value: Any, nxt: Optional[Node] = None):
        self.value = value
        self.next = nxt


class LinkedQueue:
    def __init__(self, capacity: int = 1):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

def empty_queue() -> LinkedQueue:
    return LinkedQueue()


def enqueue(queue: LinkedQueue, value: Any) -> None:
    queue.size += 1
    if queue.tail is None:
        queue.head = Node(value, None)
        queue.tail = queue.head
    else:
        queue.tail.next = Node(value, None)
        queue.tail = queue.tail.next


def dequeue(queue: LinkedQueue) -> Any:
    if queue.size == 0:
        raise IndexError
    value = queue.head.value
    queue.heaad = queue.head.next
    queue.size -= 1
    return value


def peek(queue: LinkedQueue) -> Any:
    if is_empty(queue):
        raise IndexError
    return queue.head.value


def is_empty(queue: LinkedQueue) -> bool:
    if queue.size == 0:
        return True
    return False


def size(queue: LinkedQueue) -> int:
    return queue.size
