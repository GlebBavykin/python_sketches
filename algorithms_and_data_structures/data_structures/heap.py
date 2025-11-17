from  collections import namedtuple

Entry = namedtuple('Entry', ['value', 'priority'])

class PQ:
    def __init__(self, storage_size: int):
        self.storage_size: int = storage_size
        self.storage: list[Entry | None] = [None] * (storage_size + 1)
        self.number_of_items = 0

    def put(self, value: str, priority: int):
        if self.number_of_items == self.storage_size:
            raise RuntimeError("PriorityQueue is Full")
        self.number_of_items += 1
        self.storage[self.number_of_items] = Entry(value, priority)
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



pq_example = PQ(10)
pq_example.put('Gleb', 100)
pq_example.put('Olga', 80)
pq_example.put('Kaleb', 150)
pq_example.put('Katrin', 33)
pq_example.put('Vladimir', 70)
pq_example.put('Vladislav', 71)
pq_example.put('Gleb', 101)
pq_example.put('Olga', 81)
pq_example.put('Kaleb', 151)
pq_example.put('Katrin', 31)
print(list(filter(lambda item: item is not None, [getattr(item, 'priority', None) for item in pq_example.storage])))
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(pq_example.pop())
print(list(filter(lambda item: item is not None, [getattr(item, 'priority', None) for item in pq_example.storage])))
