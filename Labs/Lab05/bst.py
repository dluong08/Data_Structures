from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Optional


class TreeNode:
    def __init__(
            self,
            value: Any,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None):
        self.value = value
        self.left = left
        self.right = right


BST = Optional[TreeNode]


def is_empty(tree: BST) -> bool:
    """ This function takes a BST as an argument and returns
        whether or not the value is tree."""
    return tree is None


def search(tree: BST, value: Any) -> bool:
    """ This fuction takes a BST and a value as arguments and
        returns whether or not the value is in the tree."""
    if tree is None:
        return False
    if tree.value == value:
        return True
    elif value < tree.value:
        if tree.left:
            return search(tree.left, value)
        else:
            return False
    else:
        if tree.right:
            return search(tree.right, value)
        else:
            return False


def insert(tree: BST, value: Any) -> BST:
    """ This function takes a BST and a vlaue as arguments and
        inserts the value into the proper location in the tree.
        That is, it will insert into the left sub-tree if the
        value is smaller than the current node's value, and
        the right sub-tree otherwise (e.g. duplicates will be
        stored on the right)."""
    if tree is None:
        return TreeNode(value)
    if value < tree.value:
        tree.left = insert(tree.left, value)
    else:
        tree.right = insert(tree.right, value)
    return tree


def delete(tree: BST, value: Any) -> BST:
    """ This function takes a BST and a value as arguments and
        deletes the value from the tree (if present) while
        preserving the binary search tree property that, for a
        given node's value, the values in the left sub-tree must
        be smaller and the values in the right sub-tree must not be
        smaller."""
    if is_empty(tree):
        return tree
    elif tree.value == value:
        if tree.right is None:
            return tree.left
        elif tree.left is None:
            return tree.right
        else:
            replace_value = find_min(tree.right)
            tree.right = delete(tree.right, replace_value)
            return TreeNode(replace_value, tree.left, tree.right)
    elif value < tree.value:
        return TreeNode(tree.value, delete(tree.left, value), tree.right)
    else:
        return TreeNode(tree.value, tree.left, delete(tree.right, value))


def find_min(tree: BST) -> Any:
    """ This function takes a BST as an argument and returns the
        smallest value in the tree. If the tree is empty, this
        function should raise a ValueError."""
    if is_empty(tree) is True:
        raise ValueError
    while tree.left is not None:
        tree = tree.left
    return tree.value
    

def find_max(tree: BST) -> Any:
    """ This function takes a BST as an argument and returns the
        smallest value in the tree. If the tree is empty, this
        function should raise a ValueError"""
    if is_empty(tree) is True:
        raise ValueError
    while tree.right is not None:
        tree = tree.right
    return tree.value

def height(tree: BST) -> int:
    """ This function takes a BST as an argument and returns the
        height of the tree. The height of a tree is measured as the
        length of the longest path from the root to a leaf. For our
        purposes, we'll say that the height of an empty tree is -1."""
    if is_empty(tree) is True:
        return -1
    else:
        left_height = height(tree.left)
        right_height = height(tree.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

def prefix_iterator(tree: BST) -> Iterator[Any]:
    """ This function takes as an argument a BST and returns an iterator
        (using yield) of the elements in prefix order wherein, for a given
        node, the node is visited before its children (visit the left child
        before the right child)."""
    if tree is not None:
        yield tree.value
        yield from prefix_iterator(tree.left)
        yield from prefix_iterator(tree.right)

def infix_iterator(tree: BST) -> Iterator[Any]:
    """ This function takes as an argument a BST and returns an iterator
        (using yield) of the elements in infix order wherein, for a given
        node, the node is visitied after its left child but before its right
        child."""
    if tree is not None:
        yield from infix_iterator(tree.left)
        yield tree.value
        yield from infix_iterator(tree.right)

def postfix_iterator(tree: BST) -> Iterator[Any]:
    """ This function takes as an argument BST and returns an iterator
        (using yield) of the elements in postfix order wherein, for a
        given node, the node is visited after its children (visit the
        left child before the right child)."""
    if tree is not None:
        yield from postfix_iterator(tree.left)
        yield from postfix_iterator(tree.right)
        yield tree.value
