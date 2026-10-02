from collections import deque
from typing import Optional, Generator

from data_structures.binary_search_tree.node import Node


def inorder_traversal_by_node(node: Optional[Node] = None) -> Generator[Node, None, None]:
    """
    Inorder traversal:
         1. Recursively traverse the entire left subtree
         2. Visit the current node
         3. Recursively traverse the entire right subtree
    """
    if node is None:
        return
    for node in inorder_traversal_by_node(node.left):
        yield node
    yield node
    for node in inorder_traversal_by_node(node.right):
        yield node


def preorder_traversal_by_value(node: Optional[Node] = None):
    """
    Pre-order traversal:
        1. Visit the current node
        2. Recursively traverse the entire left subtree
        3. Recursively traverse the entire right subtree
    """
    if node is None:
        return
    yield node.value
    for value in preorder_traversal_by_value(node.left):
        yield value
    for value in preorder_traversal_by_value(node.right):
        yield value


def inorder_traversal_by_value(node: Optional[Node] = None):
    """
    Inorder traversal:
         1. Recursively traverse the entire left subtree
         2. Visit the current node
         3. Recursively traverse the entire right subtree
    """
    if node is None:
        return
    for value in inorder_traversal_by_value(node.left):
        yield value
    yield node.value
    for value in inorder_traversal_by_value(node.right):
        yield value


def postorder_traversal_by_value(node: Optional[Node] = None):
    """
    Postorder traversal:
         1. Recursively traverse the entire left subtree
         2. Recursively traverse the entire right subtree
         3. Visit the current node

    """
    if node is None:
        return
    for value in postorder_traversal_by_value(node.left):
        yield value
    for value in postorder_traversal_by_value(node.right):
        yield value
    yield node.value


def levelorder_traversal_by_value(root: Optional[Node] = None):
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
