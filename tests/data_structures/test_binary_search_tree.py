from typing import Callable
import random
import pytest

from data_structures.binary_search_tree import (
    BSTree,
    inorder_traversal,
    levelorder_traversal,
    postorder_traversal,
    preorder_traversal,
)


@pytest.fixture(scope="function")
def binary_search_tree() -> BSTree:
    """
          50
         / \
       40   100
       /  \'    \
      9    45   120
    """
    tree = BSTree()
    tree.insert(50)
    tree.insert(100)
    tree.insert(40)
    tree.insert(120)
    tree.insert(45)
    tree.insert(9)
    return tree


@pytest.mark.parametrize(
    "traversal_method, outcome",
    [
        (preorder_traversal, [50, 40, 9, 45, 100, 120]),
        (inorder_traversal, [9, 40, 45, 50, 100, 120]),
        (postorder_traversal, [9, 45, 40, 120, 100, 50]),
        (levelorder_traversal, [50, 40, 100, 9, 45, 120]),
    ],
)
def test_binary_tree_traversal_methods(traversal_method: Callable, outcome: str, binary_search_tree: BSTree):
    """
    Test that the binary tree traversal methods work correctly.
    """
    binary_search_tree.set_traversal_method(traversal_method)
    assert list(binary_search_tree) == outcome


@pytest.mark.parametrize("expected_value", [50, 100, 40, 120, 45, 9])
def test_bst_container_protocol_1(binary_search_tree: BSTree, expected_value: int) -> None:
    """
    Test that the binary_search_tree has expected values
    """
    assert expected_value in binary_search_tree


@pytest.mark.parametrize("unexpected_value", [51, 101, 41, 121, 46, 10])
def test_bst_container_protocol_2(binary_search_tree: BSTree, unexpected_value: int) -> None:
    """
    Test that the binary_search_tree hasn't unexpected values
    """
    assert unexpected_value not in binary_search_tree


def test_binary_tree_remove(binary_search_tree: BSTree):
    """
    Test that the binary tree remove method works correctly.
    """
    tree_values = list(binary_search_tree)
    removed_value = random.choice(tree_values)
    tree_values.remove(removed_value)
    binary_search_tree.remove(removed_value)
    assert removed_value not in binary_search_tree
    assert list(binary_search_tree) == tree_values
