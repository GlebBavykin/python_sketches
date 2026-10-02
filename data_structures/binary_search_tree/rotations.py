from data_structures.binary_search_tree.node import Node


def rotate_right(node: Node) -> Node:
    """
    Rotate right around the Node:

        from:
    _____________________________
                  50
                 /
               40
               /
              9

        to:
    _____________________________
                40
               /  \
             9      50
    """
    if node.left:
        new_root = node.left
    else:
        raise ValueError("Incompatible tree structure")
    node.left = new_root.right
    new_root.right = node
    node.compute_height()
    return new_root


def rotate_left(node: Node) -> Node:
    """
    Rotate right around the Node:

        from:
    _____________________________
                9
                 \
                  40
                    \
                     50

        to:
    _____________________________
                40
               /  \
             9      50
    """
    if node.right:
        new_root = node.right
    else:
        raise ValueError("Incompatible tree structure")
    node.right = new_root.left
    new_root.left = node
    node.compute_height()
    return new_root


def rotate_left_right(node: Node) -> Node:
    """
    Rotate left and right around the Node:

        from:
    _____________________________
                50
               /
              9
                \
                40

        to:
    _____________________________
                40
               /  \
             9      50
    """
    if node.left:
        child = node.left
    else:
        raise ValueError("Incompatible tree structure")
    if child.right:
        new_root = child.right
    else:
        raise ValueError("Incompatible tree structure")
    grand1 = new_root.left
    grand2 = new_root.right
    child.right = grand1
    node.left = grand2
    new_root.left = child
    new_root.right = node
    child.compute_height()
    node.compute_height()
    return new_root


def rotate_right_left(node: Node) -> Node:
    """
    Rotate right and left around the Node:

        from:
    _____________________________
                9
                  \
                  50
                 /
                40
        to:
    _____________________________
                40
               /  \
             9      50
    """
    if node.right:
        child = node.right
    else:
        raise ValueError("Incompatible tree structure")
    if child.left:
        new_root = child.left
    else:
        raise ValueError("Incompatible tree structure")
    grand1 = new_root.left
    grand2 = new_root.right
    child.left = grand2
    node.right = grand1
    new_root.left = node
    new_root.right = child
    child.compute_height()
    node.compute_height()
    return new_root
