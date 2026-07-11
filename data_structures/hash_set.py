import collections.abc

from data_structures.hash_table import DynamicHashTable


class HashSet(collections.abc.MutableSet):
    """
    Implementation of Hash Set using DynamicHashTable
    """

    def __init__(self):
        self._data_store = DynamicHashTable()

    def __iter__(self):
        for key, value in self._data_store:
            yield key if value is True else None

    def __len__(self):
        return len(self._data_store)

    def __contains__(self, value):
        if self._data_store.get(value, False):
            return True
        else:
            return False

    def add(self, value):
        self._data_store.insert(value, True)

    def discard(self, value):
        return self._data_store.pop(value, False)
