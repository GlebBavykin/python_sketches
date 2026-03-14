import pytest

from data_structures.hash_table import DynamicHashTable


@pytest.fixture(scope="function")
def hash_table():
    """
    hash_table instance
    """
    return DynamicHashTable(capacity=100)


@pytest.fixture(scope="function")
def data():
    """
    test data
    """
    return dict(a=1, b=2, c=3)


@pytest.fixture(scope="function")
def hash_table_with_data(hash_table: DynamicHashTable, data: dict):
    """
    hash_table instance
    """
    for key, value in data.items():
        hash_table.insert(key, value)
    return hash_table


def test_insert_and_get(hash_table: DynamicHashTable, data: dict):
    """
    Add/get elements to/from hash_table
    """

    for key, value in data.items():
        hash_table.insert(key, value)

    for key in data.keys():
        assert hash_table.get(key) == data.get(key)

    assert len(hash_table) == len(data)


def test_pop(hash_table_with_data: DynamicHashTable, data: dict):
    """
    Remove elements from hash_table
    """
    for key in data.keys():
        assert hash_table_with_data.pop(key) is not None

    for key in data.keys():
        assert hash_table_with_data.get(key) is None

    assert hash_table_with_data.get("unknown_key") is None


def test_contains(hash_table_with_data: DynamicHashTable, data: dict):
    """
    Check whether hash_table contains an element from data_dict
    """
    for key in data.keys():
        assert key in hash_table_with_data

    assert "unknown_key" not in hash_table_with_data


@pytest.mark.parametrize(
    "capacity, exception",
    [(-1, ValueError), (0, ValueError), (1, ValueError), (2, ValueError)],
)
def test_boundaries_1(capacity, exception):
    """
    Check boundaries of capacity
    """
    with pytest.raises(exception):
        DynamicHashTable(capacity)


@pytest.mark.parametrize("capacity", [3])
def test_boundaries_2(capacity):
    """
    Check exceed the capacity
    """
    hash_table = DynamicHashTable(capacity=3, resizeable=False)
    for index in range(capacity + 6):
        hash_table.insert(f"key_{index}", index)
    assert len(hash_table) == capacity + 6
    assert hash_table.capacity == capacity


def test_resize():
    """
    Check resize of hash_table
    """
    hash_table = DynamicHashTable(capacity=3)
    for index in range(100):
        hash_table.insert(f"key_{index}", index)

    for index in range(100):
        assert hash_table.get(f"key_{index}") is not None
    assert "unknown_key" not in hash_table
    assert len(hash_table) == 100
    assert hash_table.capacity > 150


def test_iter(hash_table_with_data: DynamicHashTable, data: dict):
    """
    Check iteration through hash_table
    """
    for key, value in hash_table_with_data:
        assert data.get(key) == value


def test_update_value():
    """
    Check update value of the same key
    """
    hash_table = DynamicHashTable(capacity=5)
    hash_table.insert("a", 1)
    hash_table.insert("a", 2)
    assert hash_table.get("a") == 2


def test_insert_same_keys():
    """
    Check insertion of same keys in hash_table
    """

    hash_table = DynamicHashTable(capacity=5)
    for index in range(100):
        hash_table.insert("a", index)

    iterations = 0
    for iterations, item in enumerate(hash_table, start=1):
        pass
    assert len(hash_table) == 1 == iterations
    assert hash_table.get("a")
