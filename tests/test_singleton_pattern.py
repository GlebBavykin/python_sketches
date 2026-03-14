import pytest

from design_pattern.creational.singleton import Singleton


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
    Create three instances and compare them
    """
    singleton_3 = Singleton(data="Singleton instance 3")
    assert singleton_1.data == singleton_2.data == singleton_3.data
    assert singleton_1 is singleton_2 is singleton_3
