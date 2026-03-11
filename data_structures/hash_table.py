from typing import Any
from data_structures.linkedlist import DoublyLinkedList


class HashTable:
    """
        Implementation of Hash Table using Separate Chaining
    """
    def __init__(self, capacity: int = 256):
        self._size = 0
        self.capacity = capacity
        self._table: list = [None] * capacity

    def _hash(self, key: str) -> int:
        return hash(key) % self.capacity

    def insert(self, key: str, value: int) -> None:
        index: int = self._hash(key)
        if self._table[index] is None:
            linked_list = DoublyLinkedList()
            self._table[index] = linked_list.append((key, value))
        else:
            self._table[index].append((key, value))
        self._size += 1

    def get(self, key: str, default: Any = None) -> Any:
        try:
            for current_key, value in self._table[self._hash(key)]:
                if current_key == key:
                    return value
        except IndexError:
            return default
        except TypeError:
            return default

    def pop(self, key: str,  default: Any = None) -> None:
        try:
            value = self._table.pop(self._hash(key))
            self._size -= 1
            return value
        except IndexError:
            return default

    def __len__(self):
        return self._size

    def __contains__(self, key):
        if self.get(key) is None:
            return False
        else:
            return True
