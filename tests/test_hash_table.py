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

    assert hash_table_with_data.get('unknown_key') is None


def test_contains(hash_table_with_data: DynamicHashTable, data: dict):
    """
    Check whether hash_table contains an element from data_dict
    """
    for key in data.keys():
        assert key in hash_table_with_data

    assert 'unknown_key' not in hash_table_with_data


def test_resize():
    """
    Check resize of hash_table
    """
    hash_table = DynamicHashTable(capacity=5)
    for index in range(100):
        hash_table.insert(f"key_{index}", index)

    for index in range(100):
        assert hash_table.get(f"key_{index}") is not None
    assert 'unknown_key' not in hash_table
    assert len(hash_table) == 100
    assert hash_table.capacity > 150


def test_iter(hash_table_with_data: DynamicHashTable, data: dict):
    """
    Check iteration through hash_table
    """
    for key, value in hash_table_with_data:
        assert data.get(key) == value


def test_insert_same_keys(hash_table_with_data: DynamicHashTable, data: dict):
    """
    Check insertion of same keys in hash_table
    """
    hash_table = DynamicHashTable(capacity=5)
    for index in range(100):
        hash_table.insert('a', 1)
    assert len(hash_table) == 1
