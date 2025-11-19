
class Node:
    def __init__(self, value):
        self.next_node = None
        self.previous_node = None
        self.value = value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.iter_position = 0


    def append(self, value):
        new_node = Node(value)
        new_node.previous_node = self.tail
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.head.next_node = None
        else:
            new_node.next_node = self.head
            self.head = new_node
            self.head.next_node.previous_node = new_node
            self.length += 1
        return self

    def delete(self, value):
        current_node = self.head
        while current_node.next_node:
            if current_node.value == value:
                break
            current_node = current_node.next_node
        current_node.previous_node.next_node = current_node.next_node
        current_node.next_node.previous_node = current_node.previous_node
        del current_node
        self.length -= 1
        return self

    def __reversed__(self):
        current_node = self.tail
        while current_node:
            current_node.next_node, current_node.previous_node = current_node.previous_node, current_node.next_node
            current_node = current_node.next_node
        self.head, self.tail = self.tail, self.head
        return self


    def __len__(self):
        return self.length

    def __iter__(self):
        self.iter_position = 0
        return self

    def __next__(self):
        if self.iter_position == self.length:
            raise StopIteration
        else:
            current_node = self.head
            for _ in range(self.iter_position):
                current_node = current_node.next_node
            self.iter_position += 1
            return current_node.value
