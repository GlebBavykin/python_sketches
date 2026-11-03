import json
from functools import wraps
from typing import Callable


def simple_cache(func: Callable) -> Callable:
    """
    Cache without eviction policies (infinite-capacity)
    """
    cache: dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = f"({args}, {json.dumps(sorted(kwargs.items()), sort_keys=True)})"
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper
