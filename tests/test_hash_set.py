import pytest

from data_structures.hash_set import HashSet


@pytest.fixture(scope="function")
def hash_set():
    """
    Hash set instance
    """
    return HashSet()


@pytest.mark.parametrize(
    "data",
    [[1, 2, 3, 4, "a", "b", "c"], [1, 1, 2, 2, "a", "a", "b"]],
    ids=["unique", "redundant"],
)
def test_add_and_traverse(hash_set, data):
    """
    Add elements to has_set and traverse
    """
    for item in data:
        hash_set.add(item)
    assert len(hash_set) == len(set(data))
    for value in data:
        assert value in hash_set


@pytest.mark.parametrize(
    "data",
    [[1, 2, 3, 4, "a", "b", "c"], [1, 1, 2, 2, "a", "a", "b"]],
    ids=["unique", "redundant"],
)
def test_discard_and_traverse(hash_set, data):
    """
    Discard elements from has_set and traverse
    """
    for item in data:
        hash_set.add(item)
    assert len(hash_set) == len(set(data))

    for value in data:
        hash_set.discard(value)
    assert len(hash_set) == 0

    for value in data:
        assert value not in hash_set
