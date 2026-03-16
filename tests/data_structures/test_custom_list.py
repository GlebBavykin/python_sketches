import pytest

from data_structures.custom_list import CustomList


@pytest.fixture(scope="function")
def custom_list():
    """
    CustomList instance
    """
    return CustomList()


@pytest.fixture(scope="function")
def values():
    """
    Test values list
    """
    return [1, 15, 3, 2, 9, 100, 0, -1]


@pytest.fixture(scope="function")
def custom_list_with_values(values, custom_list):
    """
    Custom list with test values
    """
    for value in values:
        custom_list.append(value)
    return custom_list


def test_get_by_index(custom_list, values):
    """
    Get an element by index
    """
    for value in values:
        custom_list.append(value)
    assert len(custom_list) == len(values)

    for index in range(len(custom_list)):
        assert values[index] == custom_list[index]


def test_travers(custom_list_with_values, values):
    """
    Traverse through custom_list
    """
    for value_1, value_2 in zip(custom_list_with_values, values):
        assert value_1 == value_2


def test_pop_1(custom_list_with_values, values):
    """
    Pop elements from the right
    """
    assert custom_list_with_values.pop() == values.pop()
    assert len(custom_list_with_values) == len(values)
    assert list(custom_list_with_values) == values


def test_pop_2(custom_list):
    """
    Pop empty list
    """
    with pytest.raises(ValueError):
        custom_list.pop()
    assert len(custom_list) == 0


def test_pop_3(custom_list_with_values, values):
    """
    Pop all elements
    """
    for index in range(len(custom_list_with_values)):
        custom_list_with_values.pop()
    with pytest.raises(ValueError):
        custom_list_with_values.pop()


def test_get_index(custom_list_with_values, values):
    """
    Get index of value
    """
    assert custom_list_with_values.index(values[3]) == values.index(values[3])


def test_insert_at_position(custom_list_with_values, values):
    """
    Insert value at a specific position
    """
    custom_list_with_values.insert(2, 3)
    values.insert(2, 3)
    for value_1, value_2 in zip(custom_list_with_values, values):
        assert value_1 == value_2
    assert len(custom_list_with_values) == len(values)


def test_conver_to_string(custom_list_with_values, values):
    """
    Convert to string [1, 2, 3, ...]
    """
    assert str(custom_list_with_values) == str(values)


def test_clear(custom_list_with_values, values):
    """
    Clear list with values
    """
    custom_list_with_values.clear()
    assert len(custom_list_with_values) == 0
    with pytest.raises(ValueError):
        custom_list_with_values.pop()


def test_sort(custom_list_with_values, values):
    """
    Sort custom list with values
    """
    assert sorted(custom_list_with_values) == sorted(values)


def test_init():
    """
    Init list with multiple values
    """
    my_list = CustomList(None) * 5
    assert len(my_list) == 5
    for value in my_list:
        assert value is None
