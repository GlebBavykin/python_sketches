from collections.abc import Iterable, Iterator
from typing import Any


class MyIterator(Iterator):
    def __init__(self, collection: MyCollection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        if self._position >= len(self._collection):
            raise StopIteration()
        item = self._collection[self._position]
        self._position += 1
        return item


class MyCollection(Iterable):
    def __init__(self, collection: list[Any]):
        self._collection = collection

    def __iter__(self):
        return MyIterator(self)

    def __len__(self):
        return len(self._collection)

    def __getitem__(self, item):
        return self._collection[item]

    def add_item(self, item):
        self._collection.append(item)
