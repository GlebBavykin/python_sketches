import pytest
from algorithms_and_data_structures.data_structures.linkedlist import DoublyLinkedList


@pytest.fixture
def linked_list():
    return DoublyLinkedList()


def test_append_1(linked_list):
    values = [0, 1, 2, 3, 4, 5]
    for value in values:
        linked_list.append(value)

    current_node = linked_list.head
    for value in values:
        assert current_node.value == value
        current_node = current_node.next_node


