import ctypes


class CustomList:
    """
    Implementation of List using PyObject
    """

    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._array = self._make_array(self._capacity)
        self._iter_position = 0

    def __getitem__(self, index):
        if 0 <= index <= self._capacity:
            return self._array[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        if 0 <= index <= self._capacity:
            self._array[index] = value
        else:
            raise IndexError

    def __delitem__(self, index: int):
        if 0 <= index <= self._capacity:
            self._array[index].Delete()

    def __iter__(self):
        self._iter_position = 0
        return self

    def __next__(self):
        if self._iter_position == self._size:
            raise StopIteration
        else:
            value = self._array[self._iter_position]
            self._iter_position += 1
            return value

    def __len__(self):
        return self._size

    def __str__(self):
        result = ""
        for index in range(self._size):
            result += str(self._array[index]) + ", "
        return "[" + result[:-2] + "]"

    @staticmethod
    def _make_array(capacity):
        return (capacity * ctypes.py_object)()

    def __resize(self, capacity):
        temp = self._make_array(capacity)
        for index in range(self._capacity):
            temp[index] = self._array[index]
        self._array = temp
        self._capacity = capacity

    def append(self, value):
        if self._size == self._capacity:
            self.__resize(self._capacity * 2)
        self._array[self._size] = value
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise ValueError
        value = self._array[self._size - 1]
        self._capacity -= 1
        self._size -= 1
        return value

    def insert(self, position, value):
        if self._capacity == self._size:
            self.__resize(self._capacity * 2)

        for index in range(self._size, position, -1):
            self._array[index] = self._array[index - 1]

        self._array[position] = value
        self._size += 1

    def index(self, value):
        for index in range(self._size):
            if self._array[index] == value:
                return index
        return -1

    def clear(self):
        self._size = 0
        self._capacity = 1
        self.__resize(self._capacity * 2)
