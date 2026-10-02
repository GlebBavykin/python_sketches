import random
from typing import Callable

import pytest

from data_structures.binary_search_tree.rotations import (
    rotate_left,
    rotate_left_right,
    rotate_right,
    rotate_right_left,
)
from data_structures.binary_search_tree.simple_bst_tree import BSTree
from data_structures.binary_search_tree.traversals import (
    inorder_traversal_by_value,
    levelorder_traversal_by_value,
    postorder_traversal_by_value,
    preorder_traversal_by_value,
)

DATA_SET = [50, 100, 40, 120, 45, 9]


@pytest.fixture(scope="function")
def tree() -> BSTree:
    """
          50
         / \
       40   100
       /  \'    \
      9    45   120
    """
    return BSTree(DATA_SET)


@pytest.mark.parametrize(
    "data_set, balance_factor",
    [
        [sorted(DATA_SET), -5],
        [sorted(DATA_SET, reverse=True), 5],
    ],
    ids=[
        "right_skewed_data_set",
        "left_skewed_data_set",
    ],
)
def test_bst_skewed_tree_balance_factor(data_set: list, balance_factor: int) -> None:
    """
    Test that the bst_tree is skewed
    """
    tree = BSTree(data_set)
    if tree.root:
        assert tree.root.balance_factor == balance_factor


@pytest.mark.parametrize(
    "traversal_method, outcome",
    [
        (preorder_traversal_by_value, [50, 40, 9, 45, 100, 120]),
        (inorder_traversal_by_value, [9, 40, 45, 50, 100, 120]),
        (postorder_traversal_by_value, [9, 45, 40, 120, 100, 50]),
        (levelorder_traversal_by_value, [50, 40, 100, 9, 45, 120]),
    ],
)
def test_binary_tree_traversal_methods(traversal_method: Callable, outcome: str, tree: BSTree):
    """
    Test that the binary tree traversal methods work correctly.
    """
    tree.set_traversal_method(traversal_method)
    assert list(tree) == outcome


@pytest.mark.parametrize("expected_value", DATA_SET)
def test_bst_container_protocol_1(tree: BSTree, expected_value: int) -> None:
    """
    Test that the binary search_tree have expected values
    """
    assert expected_value in tree


@pytest.mark.parametrize("unexpected_value", [value + 1 for value in DATA_SET])
def test_bst_container_protocol_2(tree: BSTree, unexpected_value: int) -> None:
    """
    Test that the binary search tree haven't unexpected values
    """
    assert unexpected_value not in tree


def test_binary_tree_remove(tree: BSTree):
    """
    Test that the binary tree remove method works correctly.
    """
    removed_value = random.choice(list(tree))
    tree.remove(removed_value)
    assert removed_value not in tree


@pytest.mark.parametrize(
    "tree, rotation_method, outcome",
    [
        (BSTree([50, 40, 9]), rotate_right, [9, 40, 50]),
        (BSTree([9, 40, 50]), rotate_left, [9, 40, 50]),
        (BSTree([50, 9, 40]), rotate_left_right, [9, 40, 50]),
        (BSTree([9, 50, 40]), rotate_right_left, [9, 40, 50]),
    ],
)
def test_rotations(tree: BSTree, rotation_method: Callable, outcome: list):
    tree.root = rotation_method(tree.root)
    assert list(tree) == outcome
