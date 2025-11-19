import pytest
from algorithms_and_data_structures.data_structures.linkedlist import DoublyLinkedList


@pytest.fixture(scope='function')
def linked_list():
    return DoublyLinkedList()


def test_append(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values

def test_count(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert len(linked_list) == len(values) == linked_list.count()

def test_reversed(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert list(reversed(linked_list)) == list(reversed(values))


def test_iteration(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    for linked_value, list_value in zip(linked_list, values):
        assert linked_value == list_value


def test_append_left(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    extras =  [6, 7, 8, 9, 10, 11]
    for value in values:
        linked_list.append(value)
    for extra in extras:
        linked_list.append_left(extra)
        values.insert(0, extra)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values


def test_pop(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    for _ in  range(0, 5):
        assert linked_list.pop() == values.pop(0)
        assert len(linked_list) == len(values)
        assert list(linked_list) == values
    assert len(linked_list) == 0



def test_remove_1(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    linked_list.remove(3)
    values.remove(3)
    assert len(linked_list) == len(values)
    assert list(linked_list) == values

def test_remove_2(linked_list):
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
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    for value in values:
        linked_list.remove(value)
        values.remove(value)
    assert len(linked_list) == 0
