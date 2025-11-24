import pytest

from algorithms_and_data_structures.data_structures.linkedlist import DoublyLinkedList


@pytest.fixture(scope='function')
def linked_list():
    """
        DoublyLinkedList instance
    """
    return DoublyLinkedList()


def test_append(linked_list):
    """
        Add elements to linked_list from a python list from right
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values


def test_reversed(linked_list):
    """
        Reverse the linked list
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert list(reversed(linked_list)) == list(reversed(values))


def test_iteration(linked_list):
    """
        Traverse through linked list
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    for linked_value, list_value in zip(linked_list, values):
        assert linked_value == list_value


def test_append_left(linked_list):
    """
        Add elements to linked_list from a python list from left
    """
    values = [0, 1, 2, 3, 4, 5]
    extras =  [6, 7, 8, 9, 10, 11]
    for value in values:
        linked_list.append(value)
    for extra in extras:
        linked_list.append_left(extra)
        values.insert(0, extra)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values


def test_pop_1(linked_list):
    """
    Pop elements from linked list
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert linked_list.pop() == values.pop(0)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values


def test_pop_2(linked_list):
    """
    Pop head item
    """
    linked_list.append(0)
    assert linked_list.pop() == 0
    with pytest.raises(ValueError):
        linked_list.pop()
    assert len(linked_list) == 0


def test_pop_3(linked_list):
    """
    Pop all items
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    for value in values:
        assert linked_list.pop() == value
    assert len(linked_list) == 0
    with pytest.raises(ValueError):
        linked_list.pop()
    assert len(linked_list) == 0


def test_remove_1(linked_list):
    """
        Removes the first occurrence of a specific value
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    linked_list.remove(3)
    values.remove(3)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values

def test_remove_2(linked_list):
    """
    Removes not existed value
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    linked_list.remove(3)
    values.remove(3)
    with pytest.raises(ValueError):
        linked_list.remove(3)
    with pytest.raises(ValueError):
        linked_list.remove(45)


def test_remove_3(linked_list):
    """
    Removes head item
    """
    linked_list.append(0)
    linked_list.remove(0)
    assert len(linked_list) == 0
    with pytest.raises(ValueError):
        linked_list.remove(0)
    assert len(linked_list) == 0


def test_remove_4(linked_list):
    """
    Removes all items
    """
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    for value in values:
        linked_list.remove(value)
    assert len(linked_list) == 0
    with pytest.raises(ValueError):
        linked_list.pop()
    assert len(linked_list) == 0