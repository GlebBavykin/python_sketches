from collections import deque
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    """Binary Tree Node"""

    data: Any
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
    print(node.data, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)


def inorder_traversal(node: Optional[Node] = None):
    """
    Inorder traversal:
         1. Recursively traverse the entire left subtree
         2. Visit the current node
         3. Recursively traverse the entire right subtree
    """
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)


def postorder_traversal(node: Optional[Node] = None):
    """
    Postorder traversal:
         1. Recursively traverse the entire left subtree
         2. Recursively traverse the entire right subtree
         3. Visit the current node

    """
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=" ")


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
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
