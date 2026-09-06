from typing import Dict, Optional


class TreeType:
    """
    Flyweight type for trees
    """

    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def __str__(self):
        return f"{self.name} {self.color} tree with {self.texture} texture"


class Tree:
    """
    Trees with a flyweight
    """

    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def __str__(self):
        return f"{self.tree_type} based on {self.x} and {self.y} coordinates"


class TreeFactory:
    """
    Factory for trees
    """

    treeTypes: Dict[str, TreeType] = {}

    def get_tree_type(self, name: str, color: Optional[str] = None, texture: Optional[str] = None) -> TreeType:
        tree = self.treeTypes.get(name, None)
        if tree is None:
            tree = TreeType(name, color, texture)
            self.treeTypes[name] = tree
        return tree
