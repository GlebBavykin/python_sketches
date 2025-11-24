import pytest

from algorithms_and_data_structures.data_structures.heap import PQ, Entry


@pytest.fixture(scope='function')
def priority_queue():
    """
        priority_queue instance
    """
    return PQ(storage_size=6)


def test_append(priority_queue):
    """
        Add elements to linked_list from a python list from right
    """
    data = [('Haylee', 100),
            ('Cody', 80),
            ('Tatum', 150),
            ('Brayan', 33),
            ('David', 70),
            ('Tanner', 71),
    ]
    for item in data:
        priority_queue.put(*item)
    for item in sorted(data, key=lambda name: name[1], reverse=True):
        assert priority_queue.pop() == Entry(*item)
