from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next: Optional[Node] = None
    previous: Optional[Node] = None


class DoublyLinkedList:
    """
    Implementation of Doubly Linked List
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self._iter_position = 0

    def append(self, data: Any):
        """
        Add data to the right end
        """
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            if self._tail is not None:
                self._tail.next = new_node
        new_node.previous = self._tail
        self._tail = new_node
        self._length += 1
        return self

    def append_left(self, data: Any):
        """
        Add data to the left end
        """
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._head.next = None
        else:
            new_node.next = self._head
            self._head = new_node
            if self._head.next is not None:
                self._head.next.previous = new_node
            self._length += 1
        return self

    def pop(self):
        """
        Remove and return data from the right
        """
        if self._tail is not None:
            data = self._tail.data
            self.delete_node(self._tail)
        else:
            raise ValueError("List is empty")
        return data

    def pop_left(self):
        """
        Removes and returns  data from the left end
        """
        if self._head is not None:
            data = self._head.data
            self.delete_node(self._head)
        else:
            raise ValueError("List is empty")
        return data

    def delete_node(self, node: Node):
        """
        Unlink the node from linked list and delete node
        """
        if node is self._head and node.next is None and node.previous is None:
            self._head = None
            self._tail = None
            del node
        elif node is self._head and node.next is not None and node.previous is None:
            node.next.previous = None
            self._head = node.next
            del node
        elif node is self._tail and node.next is None and node.previous is not None:
            node.previous.next = None
            self._tail = node.previous
            del node
        else:
            if node.previous is not None and node.next is not None:
                node.previous.next = node.next
                node.next.previous = node.previous
            del node
        self._length -= 1

    def find(self, data: Any):
        """
        Find the first occurrence of a specific value and return node
        """
        if self._head is None:
            raise ValueError("List is empty")
        current_node = self._head
        while current_node.next:
            if current_node.data == data:
                break
            current_node = current_node.next
        if current_node is self._tail and current_node is not self._head:
            raise ValueError("data not found")
        return current_node

    def remove(self, data: Any):
        """
        Removes the first occurrence of data
        """
        found_node = self.find(data)
        self.delete_node(found_node)

    def count(self):
        """
        Returns the number of occurrences of a specific value
        """
        return self._length

    def __reversed__(self):
        current_node = self._tail
        while current_node:
            current_node.next, current_node.previous = (
                current_node.previous,
                current_node.next,
            )
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
            if self._head is not None:
                current_node = self._head
                for _ in range(self._iter_position):
                    current_node = current_node.next
                self._iter_position += 1
                return current_node.data
            else:
                raise ValueError("List is empty")
