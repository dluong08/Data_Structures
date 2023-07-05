# NOTE: Do not import anything else.
from __future__ import annotations

from typing import Any


class MaxHeap:
    def __init__(self):
        self.items = [None]


def enqueue(heap: MaxHeap, item: Any) -> None:
    """This function takes a maximum binary heap and an item as
        argumemts and adds the item to the heap in the appropriate
        position. After the function finishes, the heap should
        still satisfy the above properties. This function will not 
        return anythin. This function should have O(log n) worst case
        and O(1) average case time complexity."""
    i = size(heap) + 1
    heap.items.append(item)
    while i // 2 != 0 and heap.items[i] > heap.items[i // 2]:
        value = heap.items[i]
        heap.items[i] = heap.items[i // 2]
        heap.items[i // 2] = value
        i = i // 2


def dequeue(heap: MaxHeap) -> Any:
    """This function takes a maximum binary heap as an argument
        and removes (and returns) the largest item from the heap.
        After this function finishes, the heap should still satisfy
        the above properties. 
        
        If the heap is empty, this function should raise an IndexError
        
        This function should have O(log n) worst case time complexity"""
    if size(heap) == 0:
        raise IndexError
    elif size(heap) == 1:
        return heap.items.pop()
    value = heap.items[1]
    heap.items[1] = heap.items.pop()
    counter = 1
    cap = counter * 2
    cap_2 = counter * 2 + 1
    while (cap <= size(heap) or cap_2 <= size(heap)) and (
        heap.items[counter] < heap.items[cap] or heap.items[counter] < heap.items[cap_2]):
        if cap_2 <= size(heap) and heap.items[cap_2] > heap.items[cap]:
            value = heap.items[counter]
            heap.items[cap_2] = value
            counter = cap_2
        else:
            value = heap.items[counter]
            heap.items[counter] = heap.items[cap]
            heap.items[cap] = value
            counter = cap
        cap = counter * 2
        cap_2 = counter * 2 + 1
    return value


def peek(heap: MaxHeap) -> Any:
    """This function takes a maximum binary heap as an argument
        and returns (without removing) the largest item in the heap.
        
        If the heap is empty, this function should raise an IndexError
        
        This function should have O(1) time complexity."""
    if size(heap) == 0:
        raise IndexError
    return heap.items[1]


def size(heap: MaxHeap) -> Any:
    """This function takes the maximum binary heap as an argument
        and returns the number of items in the heap. (Note that this will
        be the size of the underlying lsit, but it will be close.)
    
        This function should have O(1) worst case time complexity."""
    return len(heap.items) - 1


# NOTE: To be used for testing
def _contents(heap: MaxHeap) -> list[Any]:
    """This function takes a maximum binary heap as an argument
        and returns a list of contents of the heap in the order they
        are stored in the heap's internal list. The return value
        should only include the "filled" spots in the list."""
    return heap.items[1:]


def heapify(lst: list[Any]) -> MaxHeap:
    """This function takes a list as an arguement and builds
        and returns a maximum binary heap out of the items
        in the list. The input list should not be modified in
        any way.
        
        This function should have O(n) worst case time complexity"""
    heap = MaxHeap()
    heap.items = [0] + lst
    index = size(heap)
    while index > 0:
        cap = index * 2
        cap_2 = index * 2 + 1
        while (cap <= size(heap) and heap.items[index] < heap.items[cap]
        ) or (cap_2 <= size(heap) and heap.items[index] < 
        heap.items[cap_2]):
            if cap_2 <= size(heap) and heap.items[cap_2] > heap.items[cap]:
                value = heap.items[index]
                heap.items[index] = heap.items[cap_2]
                heap.items[cap_2] = value
                index = cap_2
            else:
                value = heap.items[index]
                heap.items[index] = heap.items[cap]
                heap.items[cap] = value
                index = cap
            cap = index * 2
            cap_2 = index * 2 + 1
        index -= 1
    return heap


def heap_sort(lst: list[Any]) -> None:
    """This function takes a list as an argument and mutates
        the list to be sorted in ascending order. It will do
        this by building a heap with the items in the list and
        then dequeuing them back into the given list.
        
        The function should have O(nlog n) worst case time complexity"""
    for i in range(len(lst), -1, -1):
        heapify(lst)
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0] , lst[i]
        heapify(lst)
