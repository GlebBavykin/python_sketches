import pytest

from data_structures.heap import PQ


@pytest.fixture(scope="function")
def priority_queue():
    """
    priority_queue instance
    """
    return PQ(capacity=6)


@pytest.fixture(scope="function")
def data_list():
    """
    priority_queue instance
    """
    return [
        (100, "Haylee"),
        (80, "Cody"),
        (150, "Tatum"),
        (53, "Brayan"),
        (70, "David"),
        (71, "Tanner"),
    ]


def test_append_elements_to_queue(priority_queue, data_list):
    """
    Add elements to priority_queue from a python list
    """
    for item in data_list:
        priority_queue.put(*item)
    for item in sorted(data_list, reverse=True):
        assert priority_queue.pop() == item


def test_pop_from_empty_queue(priority_queue):
    """
    pop element from an empty priority_queue
    """
    with pytest.raises(IndexError):
        priority_queue.pop()


def test_exceed_queue_capacity(priority_queue, data_list):
    """
    Add too many elements to priority_queue
    """
    data_list.append((150, "Kaleb"))
    with pytest.raises(IndexError):
        for item in data_list:
            priority_queue.put(*item)
