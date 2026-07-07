import random

import pytest

from algorithms.sorting_algorithms import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)


@pytest.fixture(scope="class")
def random_number_list():
    """
    List with random numbers
    """
    return random.sample(range(0, pow(10, 4)), pow(10, 4))


@pytest.fixture(scope="class")
def sorted_random_number_list(random_number_list):
    """
    Sorted list with random numbers
    """
    return sorted(random_number_list)


def test_bubblesort_1(random_number_list, sorted_random_number_list):
    """
    Test bubblesort function
    """
    assert sorted_random_number_list == bubble_sort(random_number_list.copy())


def test_selection_sort_1(random_number_list, sorted_random_number_list):
    """
    Test selection sort function
    """
    assert sorted_random_number_list == selection_sort(random_number_list.copy())


def test_insertion_sort_1(random_number_list, sorted_random_number_list):
    """
    Test insertion sort function
    """
    assert sorted_random_number_list == insertion_sort(random_number_list.copy())


def test_quick_sort_1(random_number_list, sorted_random_number_list):
    """
    Test quick sort function
    """
    assert sorted_random_number_list == quick_sort(random_number_list.copy())


def test_merge_sort_1(random_number_list, sorted_random_number_list):
    """
    Test merge sort function
    """
    assert sorted_random_number_list == merge_sort(random_number_list.copy())
