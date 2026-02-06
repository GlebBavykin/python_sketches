import pytest

from data_structures.hash_set import HashSet


@pytest.fixture(scope="function")
def hash_set():
    """
    hash set instance
    """
    return HashSet()


def test_add_and_traverse(hash_set):
    """
    Add elements to has_set and traverse
    """
    data_in_set = [1, 2, 3, 4, 'a', 'b', 'c']
    data_out_of_set = ['d', 'e', 'f', 'g', 'h']
    for item in data_in_set:
        hash_set.add(item)
    for value in data_in_set:
        assert value in hash_set
    for data in data_out_of_set:
        assert data not in hash_set


def test_discard_and_traverse(hash_set):
    """
    Discard elements from has_set and traverse
    """
    data_in_set = [1, 2, 3, 4, 'a', 'b', 'c']
    for item in data_in_set:
        hash_set.add(item)

    for value in data_in_set:
        hash_set.discard(value)
    assert len(hash_set) == 0

    for value in data_in_set:
        assert value not in hash_set
