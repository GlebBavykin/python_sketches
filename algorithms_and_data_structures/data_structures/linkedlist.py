class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.previous_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.iter_position = 0


    def append(self, value):
        new_node = Node(value)
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            previous_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
                pass
            current_node.next_node = new_node
            new_node.previous_node = previous_node
        self.length += 1

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

    def __reversed__(self):
        current_node = self.tail
        while current_node.previous_node:
            current_node = current_node.previous_node
            print(current_node.value)

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




example = DoublyLinkedList()
example.append(0)
example.append(1)
example.append(2)
example.append(3)
print(list(example))
reversed(example)
pass
# example.append(4)
# example.append(5)
# # example.prepend(0)
# # example.prepend(15)
# # example.append(234)
# # example.delete(3)
# print(len(example))
# print(list(example))
# reversed(example)
# print(list(example))
#
#
