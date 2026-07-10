from dataclasses import dataclass
from typing import Any

from data_structures.custom_list import CustomList
from data_structures.linkedlist import DoublyLinkedList as LinkedList


@dataclass
class Entry:
    """
    Key-Value pair for Separate Chaining in DynamicHashTable
    """

    key: str
    value: Any


class DynamicHashTable:
    """
    Implementation of Hash Table using Separate Chaining
    """

    def __init__(self, capacity: int = 256, resizeable: bool = True):
        if capacity <= 2:
            raise ValueError("Capacity must be > 2")
        else:
            self._capacity = capacity
        self._resizeable = resizeable
        self._table: CustomList = CustomList(None) * capacity
        self._size = 0
        self._load_factor = 0.75
        self._threshold = self._capacity * self._load_factor

    def __len__(self):
        return self._size

    def __contains__(self, key: str):
        if self.get(key) is None:
            return False
        else:
            return True

    def __iter__(self):
        for buket in self._table:
            if buket is not None:
                for entry in buket:
                    yield entry.key, entry.value

    @property
    def capacity(self):
        return self._capacity

    def _hash(self, key: str) -> int:
        return hash(key) % self._capacity

    def _resize(self, new_size: int) -> None:
        temp = DynamicHashTable(new_size)
        for buket in self._table:
            if buket is not None:
                for entry in buket:
                    temp.insert(entry.key, entry.value)
        self._table, self._capacity = temp._table, temp._capacity
        self._threshold = self._load_factor * temp._capacity

    def insert(self, key: str, value: int) -> None:

        if self._resizeable and self._size >= self._threshold:
            self._resize(2 * self._capacity + 1)

        index: int = self._hash(key)
        # если ячейка пустая, то добавить в неё список
        if self._table[index] is None:
            self._table[index] = LinkedList().append(Entry(key, value))
            self._size += 1
        # если ячейка не пустая
        else:
            # пройти по элементам связного списка
            for entry in self._table[index]:
                # если в списке уже есть элемент с ключом key, то обновить его значение
                if entry.key == key and entry.value != value:
                    node = self._table[index].find(entry)
                    node.data.value = value
                    return
                # если в списке нет такого ключа, то добавить новый элемент в конце списка
                elif entry.key != key and entry.value != value:
                    self._table[index].append(Entry(key, value))
                    self._size += 1
                    return

    def get(self, key: str, default: Any = None) -> Any:
        try:
            for entry in self._table[self._hash(key)]:
                if entry.key == key:
                    return entry.value
        except IndexError, TypeError, KeyError:
            return default

    def pop(self, key: str, default: Any = None) -> Any:
        try:
            for entry in self._table[self._hash(key)]:
                if entry.key == key:
                    self._table[self._hash(key)].remove(entry)
                    self._size -= 1
                    return entry.value
        except IndexError, TypeError, KeyError:
            return default
