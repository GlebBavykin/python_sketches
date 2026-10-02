from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """
    Binary tree node
    """

    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None
    height: int = 0

    def compute_height(self) -> None:
        """
        Compute the height of the node in the tree
        """
        left_height = -1 if not self.left else self.left.height
        right_height = -1 if not self.right else self.right.height
        self.height = max(left_height, right_height) + 1

    @property
    def balance_factor(self) -> int:
        """
        Compute the balance factor of the node
        """
        left_height = -1 if not self.left else self.left.height
        right_height = -1 if not self.right else self.right.height
        return left_height - right_height
