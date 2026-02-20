import pytest

from design_pattern.singleton import Singleton


@pytest.fixture(scope="class")
def singleton_1():
    """
        Singleton instance
    """
    return Singleton(data="Singleton instance 1")


@pytest.fixture(scope="class")
def singleton_2():
    """
        Singleton instance
    """
    return Singleton(data="Singleton instance 2")


def test_create_two_instances(singleton_1, singleton_2):
    """
        Create two instances and compare them
    """
    assert singleton_1.get_data() == singleton_2.get_data()
    assert singleton_1 is singleton_2
