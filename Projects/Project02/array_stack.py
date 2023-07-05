from typing import Any


class ArrayStack:
    def __init__(self, capacity: int = 5):
        self.items: list[Any] = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0


def empty_stack() -> ArrayStack:
    return ArrayStack()


def push(stack: ArrayStack, value: Any) -> None:
    if stack.size >= stack.capacity:
        stack.capacity *= 2
        items_2 = [None] * stack.capacity
        for i in range(stack.size):
            items_2[i] = stack.items[i]
        stack.items = items_2
    stack.items[stack.size] = value
    stack.size += 1


def pop(stack: ArrayStack) -> Any:
    if stack.size == 0:
        raise IndexError
    return_value = stack.items[stack.size - 1]
    stack.items[stack.size - 1] = None
    stack.size -= 1
    return return_value


def peek(stack: ArrayStack) -> Any:
    if stack.is_empty():
        raise IndexError
    return stack.items[stack.size - 1]


def is_empty(stack: ArrayStack) -> bool:
    return stack.size == 0


def size(stack: ArrayStack) -> int:
    return stack.size
