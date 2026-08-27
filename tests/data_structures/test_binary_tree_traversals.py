from typing import Callable

import pytest
from _pytest.capture import CaptureFixture

from data_structures.binary_tree import (
    Node,
    inorder_traversal,
    levelorder_traversal,
    postorder_traversal,
    preorder_traversal,
)


@pytest.fixture(scope="function")
def binary_tree() -> Node:
    """
          5
         / \
       12   13
       /  \    \
      7    14   2
    """
    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)
    root.left.left = Node(7)
    root.left.right = Node(14)
    root.right.right = Node(2)
    return root


@pytest.mark.parametrize(
    "traversal_method, outcome",
    [
        (preorder_traversal, "5 12 7 14 13 2 "),
        (inorder_traversal, "7 12 14 5 13 2 "),
        (postorder_traversal, "7 14 12 2 13 5 "),
        (levelorder_traversal, "5 12 13 7 14 2 "),
    ],
)
def test_binary_tree_traversal_methods(
    traversal_method: Callable, outcome: str, binary_tree: Node, capsys: CaptureFixture
):
    """
    Test that the binary tree traversal methods work correctly.
    """
    traversal_method(binary_tree)
    assert outcome in capsys.readouterr().out
