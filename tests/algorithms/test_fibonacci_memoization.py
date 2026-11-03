import sys
from functools import lru_cache

import pytest


@lru_cache(maxsize=None)
def fibonacci(index: int) -> int:
    """
    Calculate fibonacci number
        - index grater than 970 will raise RecursionError (to fix this increase the limit sys.setrecursionlimit(5000))
    """
    if index < 0:
        raise ValueError("Index must be non-negative")
    if index <= 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


@pytest.fixture(autouse=True)
def clean_cache():
    sys.setrecursionlimit(1000)
    fibonacci.cache_clear()
    yield


def test_fibonacci_negative_index():
    """
    Test exception raised when index is negative
    """
    with pytest.raises(ValueError):
        fibonacci(-1)


@pytest.mark.skipif(sys.getrecursionlimit() > 1000, reason="Test case will fail if recursion limit exceeded 1000")
def test_fibonacci_recursion_error():
    """
    Test exception raised when recursion limit is exceeded: 1000 recursion limit depth -> 971 index
    """
    with pytest.raises(RecursionError):
        fibonacci(971)


@pytest.mark.parametrize(
    "index, result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
    ],
)
def test_fibonacci(index: int, result: int):
    """
    Calculate the Fibonacci number
    """
    assert fibonacci(index) == result


@pytest.mark.timeout(0.1)
@pytest.mark.parametrize(
    "index, result, repeats",
    [
        (100, 354224848179261915075, 1000),
        (200, 280571172992510140037611932413038677189525, 1000),
    ],
)
def test_fibonacci_memoization(index: int, result: int, repeats: int):
    """
    Calculate the Fibonacci number in less than split second using memoization
    """
    assert fibonacci(index) == result
    initial_hits = fibonacci.cache_info().hits
    initial_misses = fibonacci.cache_info().misses
    for _ in range(repeats):
        fibonacci(index)
    assert initial_hits + repeats == fibonacci.cache_info().hits
    assert initial_misses == fibonacci.cache_info().misses
