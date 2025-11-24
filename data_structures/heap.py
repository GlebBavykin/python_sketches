from collections import namedtuple

Entry = namedtuple('Entry', ['priority', 'data'])

class PQ:
    def __init__(self, queue_size: int):
        self.queue_size: int = queue_size
        self.storage: list[Entry | None] = [None] * (queue_size + 1)
        self.number_of_items = 0

    def put(self, priority: int, data: str):
        if self.number_of_items == self.queue_size:
            raise RuntimeError("PriorityQueue is Full")
        self.number_of_items += 1
        self.storage[self.number_of_items] = Entry(priority, data)
        self.swim(self.number_of_items)

    def pop(self):
        if self.number_of_items == 0:
            raise RuntimeError('PriorityQueue is Empty')
        max_priority_entry = self.storage[1]
        self.storage[1] = self.storage[self.number_of_items]
        self.storage[self.number_of_items] = None
        self.number_of_items -= 1
        self.sink(1)
        return max_priority_entry

    def sink(self, parent_index: int):
        while 2 * parent_index <= self.number_of_items:
            child_index = 2 * parent_index
            if child_index < self.number_of_items and self.left_priority_less_than_right(child_index, child_index+1):
                child_index += 1
            if not self.left_priority_less_than_right(parent_index, child_index):
                break
            self.swap_by_index(child_index, parent_index)
            parent_index = child_index

    def swim(self, child_index: int):
        while child_index > 1 and self.left_priority_less_than_right(child_index // 2, child_index):
            self.swap_by_index(child_index // 2, child_index)
            child_index = child_index // 2

    def left_priority_less_than_right(self, left_index: int, right_index: int):
        return self.storage[left_index].priority < self.storage[right_index].priority

    def swap_by_index(self, left_index: int, right_index: int):
        self.storage[left_index], self.storage[right_index] = self.storage[right_index], self.storage[left_index]
