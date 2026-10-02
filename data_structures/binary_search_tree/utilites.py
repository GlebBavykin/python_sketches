from data_structures.binary_search_tree.node import Node
from data_structures.binary_search_tree.rotations import (
    rotate_left,
    rotate_left_right,
    rotate_right,
    rotate_right_left,
)


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


def rebalance_left_leaning(node: Node):
    """
    Rebalance left heavy node
    """
    if node.balance_factor == 2:
        if node.left:
            if node.left.balance_factor >= 0:
                node = rotate_right(node)
            else:
                node = rotate_left_right(node)
        else:
            raise ValueError("Incompatible tree structure")
    return node


def rebalance_right_leaning(node: Node):
    """
    Rebalance right heavy node
    """
    if node.balance_factor == -2:
        if node.right:
            if node.right.balance_factor <= 0:
                node = rotate_left(node)
            else:
                node = rotate_right_left(node)
        else:
            raise ValueError("Incompatible tree structure")
    return node
