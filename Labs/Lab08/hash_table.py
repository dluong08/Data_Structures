from __future__ import annotations

from collections.abc import Callable, Hashable
from typing import Any, List, Tuple


# An entry in the hash table is a key-value pair
HashEntry = Tuple[Hashable, Any]
# Each entry in the hash table array will be a list of HashEntry pairs
HashChain = List[HashEntry]


class HashTable:
    """A hash table with separate chaining."""
    def __init__(
            self,
            capacity: int = 10,
            hash_function: Callable[[Hashable], int] = hash):
        """Creates an empty hash table.

        Args:
            capacity:
                The initial capacity of the backing array.  The default
                capacity is 10.
            hash_function:
                The function to use to compute hash values for the given
                keys.  The default hash function is the Python builtin
                hash function.
        """
        self.table: list[HashChain] = [[] for _ in range(capacity)]

        self.size: int = 0
        self.capacity: int = capacity
        self.hash_function = hash_function


# NOTE: Computing the hash value of the key could be slow, we should
# only do it once.
def insert(hash_table: HashTable, key: Hashable, value: Any) -> None:
    index = hash_table.hash_function(key) % hash_table.capacity
    x = True
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            hash_table.table[index][i] = (key, value)
            x = False
    if load_factor(hash_table) >= 1.0 and x:
        position = [[] for _ in range(hash_table.capacity * 2)]
        for i in range(hash_table.capacity):
            lst = hash_table.table[i]
            for j in range(len(lst)):
                tup = lst[j]
                new_index = hash_table.hash_function(tup[0]) % (
                    hash_table.capacity * 2
                )
                position[new_index].append((tup[0], tup[1]))
        hash_table.table = position
        hash_table.capacity *= 2
    if x:
        hash_table.table[index].append((key, value))
        hash_table.size += 1


def get_item(hash_table: HashTable, key: Hashable) -> Any:
    index = hash_table.hash_function(key) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            return hash_table.table[index][i][1]
    raise KeyError


def contains(hash_table: HashTable, key: Hashable) -> bool:
    index = hash_table.hash_function(key) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            return True
    return False


def remove(hash_table: HashTable, key: Hashable) -> tuple[Hashable, Any]:
    index = hash_table.hash_function(key) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            hash_table.size -= 1
            return hash_table.table[index].pop(i)
    raise KeyError


def size(hash_table: HashTable) -> int:
    return hash_table.size


def keys(hash_table: HashTable) -> list[Hashable]:
    lst = []
    for i in hash_table.table:
        for j in i:
            lst.append(j[0])
    return lst


def load_factor(hash_table: HashTable) -> float:
    return hash_table.size / hash_table.capacity


def _contents(hash_table: HashTable) -> list[HashChain]:
    lst = []
    for i in hash_table.table:
        lst.append(i)
    return lst
