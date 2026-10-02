from data_structures.binary_search_tree.node import Node
from data_structures.binary_search_tree.simple_bst_tree import BSTree
from data_structures.binary_search_tree.utilites import rebalance_left_leaning, rebalance_right_leaning, remove_min_node


class AVLTree(BSTree):
    """
    AVL Binary search tree
    """

    def _insert(self, node: Node | None, value: int) -> Node:
        """
        Auxiliary method to insert the value into the tree
        """
        if node is None:
            return Node(value)

        if value <= node.value:
            node.left = self._insert(node.left, value)
            node = rebalance_left_leaning(node)
        else:
            node.right = self._insert(node.right, value)
            node = rebalance_right_leaning(node)
        if node:
            node.compute_height()
        return node

    def _remove(self, node: Node | None, value: int):
        """
        Auxiliary method to remove the value from the tree
        """
        if node is None:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)
            node = rebalance_right_leaning(node)
        elif value > node.value:
            node.right = self._remove(node.right, value)
            node = rebalance_left_leaning(node)
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
                node = rebalance_left_leaning(node)
        if node:
            node.compute_height()
        return node
