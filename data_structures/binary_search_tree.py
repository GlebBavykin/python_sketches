from collections import deque
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Node:
    """
    Binary tree node
    """

    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def preorder_traversal(node: Optional[Node] = None):
    """
    Pre-order traversal:
        1. Visit the current node
        2. Recursively traverse the entire left subtree
        3. Recursively traverse the entire right subtree
    """
    if node is None:
        return
    yield node.value
    for value in preorder_traversal(node.left):
        yield value
    for value in preorder_traversal(node.right):
        yield value


def inorder_traversal(node: Optional[Node] = None):
    """
    Inorder traversal:
         1. Recursively traverse the entire left subtree
         2. Visit the current node
         3. Recursively traverse the entire right subtree
    """
    if node is None:
        return
    for value in inorder_traversal(node.left):
        yield value
    yield node.value
    for value in inorder_traversal(node.right):
        yield value


def postorder_traversal(node: Optional[Node] = None):
    """
    Postorder traversal:
         1. Recursively traverse the entire left subtree
         2. Recursively traverse the entire right subtree
         3. Visit the current node

    """
    if node is None:
        return
    for value in postorder_traversal(node.left):
        yield value
    for value in postorder_traversal(node.right):
        yield value
    yield node.value


def levelorder_traversal(root: Optional[Node] = None):
    """
    Level order traversal processes a tree level by level from top to bottom and left to right using a Queue data structure:
        1. Check if empty
        2. Initialize queue
        3. Loop while queue is not empty:
            - Dequeue (remove) the front node from the queue
            - Process the node (such as printing or saving its value)
            - Enqueue (add) the node's left child to the queue if it exists
            - Enqueue the node's right child to the queue if it exists
        4. Repeat
    """
    if root is None:
        return
    queue = deque([root])
    while queue:
        node: Node = queue.popleft()
        yield node.value
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def remove_min_node(node: Node | None) -> Node | None:
    """
    Remove the minimum node in tree
    """
    if node is None:
        return None
    if node.left is None:
        return node.right
    node.left = remove_min_node(node.left)
    return node


def remove_max_node(node: Node | None) -> Node | None:
    """
    Remove the maximum node in tree
    """
    if node is None:
        return None
    if node.right is None:
        return node.left
    node.right = remove_max_node(node.right)
    return node


class BSTree:
    """
    Binary search tree
    """

    def __init__(self):
        self._root = None
        self._traversal_method: Callable = inorder_traversal
        self._remove_method = remove_min_node

    def __contains__(self, value: int) -> bool:
        node = self._root
        while node:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def __iter__(self):
        yield from self._traversal_method(self._root)

    def set_traversal_method(self, method: Callable):
        """
        Set the traversal method for __iter__ protocol
        """
        self._traversal_method = method

    def insert(self, value: int) -> None:
        """
        Insert the value into the tree
        """
        self._root = self._insert(self._root, value)

    def _insert(self, node: Node | None, value: int) -> Node:
        """
        Auxiliary method to insert the value into the tree
        """
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def remove(self, value: int):
        """
        Removes the value from the tree
        """
        self._root = self._remove(self._root, value)

    def _remove(self, node: Node | None, value: int):
        """
        Auxiliary method to remove the value from the tree
        """
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            original, node = node, node.right

            while node.left:
                node = node.left

            node.right = remove_min_node(original.right)
            node.left = original.left
        return node
