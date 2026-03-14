import collections.abc

from data_structures.hash_table import DynamicHashTable


class HashSet(collections.abc.MutableSet):
    """
    Implementation of Hash Set using Python dict
    """

    def __init__(self):
        self._data_store = DynamicHashTable()

    def __iter__(self):
        for key, value in self._data_store:
            yield key if value is True else None

    def __len__(self):
        return len(self._data_store)

    def __contains__(self, element):
        if self._data_store.get(element, False):
            return True
        else:
            return False

    def add(self, element):
        self._data_store.insert(element, True)

    def discard(self, element):
        return self._data_store.pop(element, False)
