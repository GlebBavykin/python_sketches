from dataclasses import dataclass
from typing import Optional, Any, Tuple

from data_structures.custom_list import CustomList


@dataclass
class Entry:
    """
    Element in a queue
    """

    priority: int
    data: str

    def __init__(self, priority: int, data: str):
        self.priority = priority
        self.data = data

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __setitem__(self, b):
        self.priority = b.priority
        self.data = b.data

    def __getitem__(self):
        return self


class PQ:
    """
    Implementation of Heap Priority Queue
    """

    def __init__(self, capacity: int = 5, resizeable: bool = True) -> None:
        if capacity <= 2:
            raise ValueError("Capacity must be > 2")
        else:
            self._capacity = capacity
        self._storage: CustomList[Optional[Entry]] = CustomList(None) * (capacity + 1)
        self._size = 0
        self._resizeable = resizeable

    def __len__(self):
        return self._size

    @property
    def resizeable(self):
        return self._resizeable

    @resizeable.setter
    def resizeable(self, value: bool):
        self._resizeable = value

    def put(self, priority: int, data: Any) -> None:
        if self._size == self._capacity:
            if self._resizeable:
                self._resize(self._capacity * 2)
            else:
                raise IndexError("Priority Queue is Full")
        self._size += 1
        self._storage[self._size] = Entry(priority, data)
        self._swim(self._size)

    def pop(self) -> Tuple[int, Any]:
        if self._size == 0:
            raise IndexError("Priority Queue is Empty")
        element = self._storage[1]
        self._storage[1], self._storage[self._size] = self._storage[self._size], None
        self._size -= 1
        self._sink(1)
        return element.priority, element.data

    def _sink(self, parent_index: int):
        while parent_index * 2 <= self._size:
            child_index = parent_index * 2
            if self._storage[parent_index] > self._storage[child_index]:
                break
            if child_index < self._size:
                if self._storage[child_index] < self._storage[child_index + 1]:
                    child_index += 1
            self._swap(parent_index, child_index)
            parent_index = child_index

    def _swim(self, child_index: int):
        while child_index > 1:
            parent_index = child_index // 2
            if self._storage[parent_index] > self._storage[child_index]:
                break
            self._swap(parent_index, child_index)
            child_index = parent_index

    def _swap(self, p_index: int, c_index: int):
        self._storage[p_index], self._storage[c_index] = self._storage[c_index], self._storage[p_index]

    def _resize(self, new_capacity: int) -> None:
        temp = PQ(capacity=new_capacity, resizeable=self._resizeable)
        for entry in self._storage:
            if entry is not None:
                temp.put(entry.priority, entry.data)
        self._size, self._capacity, self._storage = temp._size, temp._capacity, temp._storage
