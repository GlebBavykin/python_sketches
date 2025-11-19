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

    current_node = linked_list.head
    for value in values:
        assert current_node.value == value
        current_node = current_node.next_node


def test_reversed(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)

    reversed(linked_list)
    current_node = linked_list.head
    for value in reversed(values):
        assert current_node.value == value
        current_node = current_node.next_node


def test_iteration(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)
    assert list(linked_list) == values
    for linked_value, list_value in zip(linked_list, values):
        assert linked_value == list_value
