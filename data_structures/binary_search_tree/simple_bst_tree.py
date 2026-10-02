from typing import Callable, Iterable, Optional

from data_structures.binary_search_tree.node import Node
from data_structures.binary_search_tree.traversals import inorder_traversal_by_value
from data_structures.binary_search_tree.utilites import remove_min_node


class BSTree:
    """
    Simple Binary search tree
    """

    def __init__(self, values: Iterable | None = None):
        self.root: Optional[Node] = None
        self._traversal_method: Callable = inorder_traversal_by_value
        self._remove_method = remove_min_node
        if values:
            for value in values:
                self.insert(value)

    def __contains__(self, value: int) -> bool:
        node = self.root
        while node:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def __iter__(self):
        yield from self._traversal_method(self.root)

    def set_traversal_method(self, method: Callable):
        """
        Set the traversal method for __iter__ protocol
        """
        self._traversal_method = method

    def insert(self, value: int) -> None:
        """
        Insert the value into the tree
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node: Node | None, value: int) -> Node:
        """
        Auxiliary method to insert the value into the tree
        """
        if node is None:
            return Node(value)

        if value <= node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        if node:
            node.compute_height()
        return node

    def remove(self, value: int):
        """
        Removes the value from the tree
        """
        self.root = self._remove(self.root, value)

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
        if node:
            node.compute_height()
        return node
