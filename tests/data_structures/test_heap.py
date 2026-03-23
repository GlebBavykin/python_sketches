import pytest

from data_structures.heap import PQ


@pytest.fixture(scope="function")
def priority_queue():
    """
    priority_queue instance
    """
    return PQ(capacity=3)


@pytest.fixture(scope="function")
def data_list():
    """
    priority_queue instance
    """
    return [
        (100, "Haylee"),
        (80, "Cody"),
        (150, "Tatum"),
        (53, "Bryan"),
        (70, "David"),
        (71, "Tanner"),
    ]


def test_append_elements_to_queue(priority_queue, data_list):
    """
    Add elements to min priority_queue from a python list
    """
    for item in data_list:
        priority_queue.put(*item)
    assert len(priority_queue) == len(data_list)
    for item in sorted(data_list, reverse=True):
        assert priority_queue.pop() == item


def test_max_heap(priority_queue, data_list):
    """
    Add elements to max priority_queue from a python list
    """
    priority_queue = PQ(max_heap=True)
    for item in data_list:
        priority_queue.put(*item)
    assert len(priority_queue) == len(data_list)
    for item in sorted(data_list):
        assert priority_queue.pop() == item


def test_pop_from_empty_queue(priority_queue):
    """
    pop element from an empty priority_queue
    """
    assert len(priority_queue) == 0
    with pytest.raises(IndexError):
        priority_queue.pop()


def test_not_exceed_queue_capacity(priority_queue, data_list):
    """
    Add too many elements to priority_queue
    """
    priority_queue.resizeable = False
    data_list.append((150, "Kaleb"))
    with pytest.raises(IndexError):
        for item in data_list:
            priority_queue.put(*item)
