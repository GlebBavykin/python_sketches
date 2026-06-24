import pytest

from design_patterns.structural.flyweight import Tree, TreeFactory


@pytest.fixture(scope="class")
def tree_factory() -> TreeFactory:
    """
    TreeFactory with two trees
    """
    instance = TreeFactory()
    instance.get_tree_type("pine", "green", "light")
    instance.get_tree_type("fir", "green", "grain")
    return instance


def test_flyweight(tree_factory: TreeFactory) -> None:
    """
    Check flyweight tree in every instance of trees
    """
    trees = []

    # Plant trees on the diagonal
    for x, y in zip(range(1000), range(1000)):
        for name in ["pine", "fir"]:
            trees.append(Tree(x, y, tree_factory.get_tree_type(name)))

    # Check that all trees has the same instance from tree_factory
    for name in ["pine", "fir"]:
        for tree in trees:
            if tree.tree_type.name == name:
                assert tree.tree_type is tree_factory.get_tree_type(name)
