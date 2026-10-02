import random

import pytest

from data_structures.binary_search_tree.avl_tree import AVLTree
from data_structures.binary_search_tree.traversals import inorder_traversal_by_node

DATA_SET = [50, 100, 40, 120, 45, 9]


@pytest.fixture(scope="function")
def tree() -> AVLTree:
    return AVLTree(DATA_SET)


@pytest.mark.parametrize(
    "data_set",
    [
        sorted(DATA_SET),
        sorted(DATA_SET, reverse=True),
        DATA_SET,
    ],
    ids=[
        "right_skewed_data_set",
        "left_skewed_data_set",
        "balanced_data",
    ],
)
def test_avl_balance_factor(data_set: list) -> None:
    """
    Test that the avl_tree is balanced
    """
    tree = AVLTree(data_set)
    tree.set_traversal_method(inorder_traversal_by_node)
    for node in tree:
        assert -1 <= node.balance_factor <= 1


@pytest.mark.parametrize("expected_value", DATA_SET)
def test_avl_container_protocol_1(tree: AVLTree, expected_value: int) -> None:
    """
    Test that the avl_tree have expected values
    """
    assert expected_value in tree


@pytest.mark.parametrize("unexpected_value", [value + 1 for value in DATA_SET])
def test_avl_container_protocol_2(tree: AVLTree, unexpected_value: int) -> None:
    """
    Test that the tree haven't unexpected values
    """
    assert unexpected_value not in tree


def test_avl_tree_remove(tree: AVLTree):
    """
    Test that the binary tree remove method works correctly
    """
    removed_value = random.choice(list(tree))
    tree.remove(removed_value)
    assert removed_value not in tree
