import pytest

from data_structures.hash_table import HashTable


@pytest.fixture(scope="function")
def hash_table():
    """
    hash_table instance
    """
    return HashTable(capacity=100)


@pytest.fixture(scope="function")
def data():
    """
    test data
    """
    return dict(a=1, b=2, c=3)


@pytest.fixture(scope="function")
def hash_table_with_data(hash_table: HashTable, data: dict):
    """
    hash_table instance
    """
    for key, value in data.items():
        hash_table.insert(key, value)
    return hash_table


def test_insert_and_get(hash_table: HashTable, data: dict):
    """
    Add/get elements to/from hash_table
    """

    for key, value in data.items():
        hash_table.insert(key, value)

    for key in data.keys():
        assert hash_table.get(key) == data.get(key)

    assert len(hash_table) == len(data)


def test_pop(hash_table_with_data: HashTable, data: dict):
    """
    Remove elements from hash_table
    """
    for key in data.keys():
        hash_table_with_data.pop(key)

    for key in data.keys():
        assert hash_table_with_data.get(key) is None

    assert hash_table_with_data.get('unknown_key') is None


def test_contains(hash_table_with_data: HashTable, data: dict):
    """
    Check whether hash_table contains an element from data_dict
    """
    for key in data.keys():
        assert key in hash_table_with_data

    assert 'unknown_key' not in hash_table_with_data