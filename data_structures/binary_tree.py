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
