from typing import Any, Optional, Self, Tuple

from data_structures.custom_list import CustomList


class Entry:
    """
    Element in a queue
    """

    def __init__(self, priority: int, data: Any) -> None:
        self.priority = priority
        self.data = data

    def __lt__(self, other) -> bool:
        return self.priority < other.priority

    def __gt__(self, other) -> bool:
        return self.priority > other.priority

    def __eq__(self, other) -> bool:
        return self.priority == other.priority

    def __setitem__(self, other) -> None:
        self.priority = other.priority
        self.data = other.data

    def __getitem__(self) -> Self:
        return self


class PQ:
    """
    Implementation of Heap Priority Queue
    """

    def __init__(self, capacity: int = 5, resizeable: bool = True, max_heap: bool = False) -> None:
        if capacity <= 2:
            raise ValueError("Capacity must be > 2")
        else:
            self._capacity = capacity
        self._storage: CustomList = CustomList(None) * (capacity + 1)
        self._size = 0
        self._resizeable = resizeable
        self._max_heap = max_heap

    def __len__(self):
        return self._size

    def _swap(self, p_index: int, c_index: int) -> None:
        """
        Swaps two elements at p_index and c_index positions
        """
        self._storage[p_index], self._storage[c_index] = self._storage[c_index], self._storage[p_index]

    def _swim(self, child_index: int) -> None:
        """
        Lowers node to the desired tree level
        """
        while child_index > 1:
            parent_index = child_index // 2
            if self._storage[parent_index] > self._storage[child_index]:
                break
            self._swap(parent_index, child_index)
            child_index = parent_index

    def _sink(self, parent_index: int) -> None:
        """
        Lifts the element up to the desired tree level
        """
        while parent_index * 2 <= self._size:
            child_index = parent_index * 2
            if self._storage[parent_index] > self._storage[child_index]:
                break
            if child_index < self._size:
                if self._storage[child_index] < self._storage[child_index + 1]:
                    child_index += 1
            self._swap(parent_index, child_index)
            parent_index = child_index

    def _resize(self, new_capacity: int) -> None:
        """
        Resizes the priority queue to the new capacity
        """
        temp = PQ(capacity=new_capacity, resizeable=self._resizeable)
        for entry in self._storage:
            if entry is not None:
                temp.put(entry.priority, entry.data)
        self._size, self._capacity, self._storage = temp._size, temp._capacity, temp._storage

    @property
    def resizeable(self):
        return self._resizeable

    @resizeable.setter
    def resizeable(self, value: bool):
        self._resizeable = value

    def put(self, priority: int, data: Any) -> None:
        """
        Put an element into the priority queue
        """
        if self._size == self._capacity:
            if self._resizeable:
                self._resize(self._capacity * 2)
            else:
                raise IndexError("Queue is full")
        self._size += 1
        if self._max_heap:
            entry = Entry(-priority, data)
        else:
            entry = Entry(priority, data)
        self._storage[self._size] = entry
        self._swim(self._size)

    def pop(self) -> Tuple[int, Any]:
        """
        Pop an element from the priority queue
        """
        if self._size == 0:
            raise IndexError("Queue is empty")
        entry = self._storage[1]
        self._storage[1], self._storage[self._size] = self._storage[self._size], None
        self._size -= 1
        self._sink(1)
        if self._max_heap:
            return -entry.priority, entry.data
        return entry.priority, entry.data
