from __future__ import annotations

from typing import Any, Optional


class Node:
    """Represents a node to be used in a doubly linked list."""
    def __init__(
            self,
            value: Any,
            prev: Optional[Node] = None,
            nxt: Optional[Node] = None):
        self.value = value

        # NOTE: This means that if prev and nxt are None, self.prev and
        # self.next will be self.  You may find this useful.  This means
        # that self.prev and self.next aren't Optional Nodes, they are
        # always Nodes.
        self.prev: Node = prev or self
        self.next: Node = nxt or self


class OrderedList:
    """A circular, doubly linked list of items, from lowest to highest.
    The contents of the list *must* have a accurate notation of less
    than and of equality.  That is to say, the contents of the list must
    implement both __lt__ and __eq__.
    """
    def __init__(self):
        self.head = Node("dummy")
        self.size = 0


def insert(lst: OrderedList, value: Any) -> None:
    """ This function takes an ordered list and a value as arguemnts and
    inserts the value into the proper location in the list"""
    original_node = lst.head
    current_node = lst.head.next
    while original_node != current_node and value >= current_node.value:
        current_node = current_node.next
    new_node = Node(value, current_node.prev, current_node)
    current_node.prev.next = new_node
    current_node.prev = new_node
    lst.size += 1


def remove(lst: OrderedList, value: Any) -> None:
    """ This function takes an ordered lsit and a value as arguments and
    removes the value from the list. If the value is not in the list,
    then this function should raise a ValueError"""
    current_node = lst.head.next
    current_length = 0
    while (current_node.value != value) and (current_length < lst.size):
        current_node = current_node.next
        current_length += 1
    if current_length == lst.size:
        raise ValueError
    current_node.prev.next = current_node.next
    current_node.next.prev = current_node.prev
    lst.size -= 1


def contains(lst: OrderedList, value: Any) -> bool:
    """ This function takes an ordered list and a value as arguments and
    returns whether or not the vlaue is in the list (True if it is, False
    otherwise)"""
    current_node = lst.head.next
    current_length = 0
    while (current_node.value != value) and (current_length < lst.size):
        current_node = current_node.next
        current_length += 1
    return current_node.value == value


def index(lst: OrderedList, value: Any) -> int:
    """ This function takes an ordered list and a value as arguments and
    and returns the index  of the first occurrence of the value in the list.
    If the value is not in the list, then this function should raise a
    ValueError"""
    current_node = lst.head.next
    counter = 0
    while current_node.value != value and counter < lst.size:
        current_node = current_node.next
        counter += 1
    if counter == lst.size:
        raise ValueError
    return counter


def get(lst: OrderedList, index: int) -> Any:
    """ This function takes an ordered list and an index as arguments and
    and returns the value at the given index. If the index is outside the
    bounds of the list, then this function should raise an IndexError."""
    if index >= lst.size or index < 0:
        raise IndexError
    current_node = lst.head.next
    counter = 0
    while counter != index:
        current_node = current_node.next
        counter += 1
    return current_node.value


def pop(lst: OrderedList, index: int) -> Any:
    """ This function takes an ordered list and an index as arguments and
    removes (and return) the value at the given index. If the index is
    outside the bounds of the list, then this function should raise an
    IndexError"""
    if index >= lst.size or index < 0:
        raise IndexError
    current_node = lst.head.next
    counter = 0
    while counter != index:
        current_node = current_node.next
        counter += 1
    value = current_node.value
    current_node.prev.next = current_node.next
    current_node.next.prev = current_node.prev
    lst.size -= 1
    return value


def is_empty(lst: OrderedList) -> bool:
    """ This function takes an ordered list as an arguemnt and returns
    whether or not the list is empty (True if it is, False otherwise)"""
    return lst.size == 0


def size(lst: OrderedList) -> int:
    """ This function takes an ordered list as an argument and returns
    the number of items in the list."""
    return lst.size
