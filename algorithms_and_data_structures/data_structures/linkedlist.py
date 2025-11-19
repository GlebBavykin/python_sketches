
class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self._iter_position = 0


    def append(self, data):
        new_node = Node(data)
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

    def prepend(self, data):
        new_node = Node(data)
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
        data = self._head.data
        next_node = self._head.next
        del self._head
        self._head = next_node
        self._length -= 1
        return data

    def delete(self, data):
        current_node = self._head
        while current_node.next:
            if current_node.data == data:
                break
            current_node = current_node.next
        current_node.previous.next = current_node.next
        current_node.next.previous = current_node.previous
        del current_node
        self._length -= 1
        return self

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
            return current_node.data
