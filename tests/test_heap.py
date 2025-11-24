import pytest

from data_structures.heap import PQ, Entry


@pytest.fixture(scope='function')
def priority_queue():
    """
        priority_queue instance
    """
    return PQ(queue_size=6)


def test_append(priority_queue):
    """
        Add elements to priority_queue from a python list
    """
    data = [(100, 'Haylee'),
            (80, 'Cody'),
            (150, 'Tatum'),
            (53, 'Brayan'),
            (70, 'David'),
            (71, 'Tanner'),
    ]
    for item in data:
        priority_queue.put(*item)
    for item in sorted(data, reverse=True):
        assert priority_queue.pop() == Entry(*item)
