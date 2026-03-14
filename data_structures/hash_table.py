from typing import Any

from data_structures.linkedlist import DoublyLinkedList


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
        self._table: list = [None] * capacity
        self._size = 0
        self._load_factor = 0.75
        self._threshold = self._capacity * self._load_factor

    def __len__(self):
        return self._size

    def __contains__(self, key):
        if self.get(key) is None:
            return False
        else:
            return True

    def __iter__(self):
        for buket in self._table:
            if buket is not None:
                for key, value in buket:
                    yield key, value

    @property
    def capacity(self):
        return self._capacity

    def _hash(self, key: str) -> int:
        return hash(key) % self._capacity

    def _resize(self, new_size: int) -> None:
        temp = DynamicHashTable(new_size)
        for buket in self._table:
            if buket is not None:
                for key, value in buket:
                    temp.insert(key, value)
        self._table, self._capacity = temp._table, temp._capacity
        self._threshold = self._load_factor * temp._capacity

    def insert(self, key: str, value: int) -> None:

        if self._resizeable and self._size >= self._threshold:
            self._resize(2 * self._capacity + 1)

        index: int = self._hash(key)
        # если ячейка пустая, то добавить в неё список
        if self._table[index] is None:
            self._table[index] = DoublyLinkedList().append((key, value))
            self._size += 1
        # если ячейка не пустая
        else:
            # пройти по элементам связного списка
            for current_key, current_value in self._table[index]:
                # если в списке уже есть элемент с ключом key, то обновить его значение
                if key == current_key and current_value != value:
                    node = self._table[index].find((current_key, current_value))
                    node.data = (key, value)
                    break
                elif current_key == key and current_value == value:
                    pass
                else:
                    self._table[index].append((key, value))
                    self._size += 1
                    break

    def get(self, key: str, default: Any = None) -> Any:
        try:
            for current_key, value in self._table[self._hash(key)]:
                if current_key == key:
                    return value
        except IndexError, TypeError, KeyError:
            return default

    def pop(self, key: str, default: Any = None) -> None:
        try:
            for current_key, value in self._table[self._hash(key)]:
                if current_key == key:
                    self._table[self._hash(key)].remove((key, value))
                    self._size -= 1
                    return value
        except IndexError, TypeError, KeyError:
            return default
