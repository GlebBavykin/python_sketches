import pytest

from design_patterns.behavioral.iterator_pattern import MyCollection


@pytest.fixture(scope="function")
def data() -> list[int]:
    """
    List of test data
    """
    return [1, 2, 3]


@pytest.fixture(scope="function")
def my_collection(data) -> MyCollection:
    """
    Create MyCollection with data in it
    """
    return MyCollection(data)


def test_iterator_pattern_1(my_collection: MyCollection, data: list[int]):
    """
    Test iterator pattern: traverse through MyCollection and pyton list simultaneously
    """
    for collection_item, data_item in zip(my_collection, data):
        assert collection_item == data_item
