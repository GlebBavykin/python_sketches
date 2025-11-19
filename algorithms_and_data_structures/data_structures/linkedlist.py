from typing import Any


class Node:
    def __init__(self, item: Any):
        self.next = None
        self.previous = None
        self.item = item

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self._iter_position = 0


    def append(self, item: Any):
        """
            Adds an item to the right end
        """
        new_node = Node(item)
        new_node.previous = self._tail
        self._tail = new_node
        if self._head is None:
            self._head = new_node
        else:
            current_node = self._head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self._length += 1
        return self

    def append_left(self, item: Any):
        """
            Adds an item to the left end
        """
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._head.next = None
        else:
            new_node.next = self._head
            self._head = new_node
            self._head.next.previous = new_node
            self._length += 1
        return self

    def pop(self):
        """
            Removes and returns an item from the right end
        """
        item = self._head.item
        next_node = self._head.next
        del self._head
        self._head = next_node
        next_node.previous = self._head
        self._length -= 1
        return item

    def pop_left(self):
        """
            Removes and returns an item from the left end
        """
        item = self._head.item
        next_node = self._head.next
        del self._head
        self._head = next_node
        next_node.previous = self._head
        self._length -= 1
        return item

    def rotate(self, n: int):
        """
            Rotates the deque n steps to the right (positive n) or left (negative n)
        """
        pass

    def remove(self, item: Any):
        """
            Removes the first occurrence of a value
        """
        current_node = self._head
        while current_node.next:
            if current_node.item == item:
                break
            current_node = current_node.next
        try:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
            del current_node
        except AttributeError:
            raise ValueError("value not found")
        self._length -= 1
        return self

    def count(self):
        """
            Returns the number of occurrences of a specific value
        """
        return self._length

    def __reversed__(self):
        current_node = self._tail
        while current_node:
            current_node.next, current_node.previous = current_node.previous, current_node.next
            current_node = current_node.next
        self._head, self._tail = self._tail, self._head
        return self

    def __len__(self):
        return self._length

    def __iter__(self):
        self._iter_position = 0
        return self

    def __next__(self):
        if self._iter_position == self._length:
            raise StopIteration
        else:
            current_node = self._head
            for _ in range(self._iter_position):
                current_node = current_node.next
            self._iter_position += 1
            return current_node.item
