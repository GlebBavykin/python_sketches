import collections.abc


class HashSet(collections.abc.MutableSet):
    """
        Implementation of Hash Set using Python dict
    """
    def __init__(self, data: dict = None):
        if data is None:
            self.data_store = dict()
        else:
            self.data_store = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        data_list = list(self.data_store.keys())
        try:
            item = data_list[self.index]
            self.index += 1
            return item
        except IndexError:
            raise StopIteration

    def discard(self, a):
        return self.data_store.pop(a, False)

    def __len__(self):
        return len(self.data_store)

    def __contains__(self, a):
        if self.data_store.get(a, False):
            return True
        else:
            return False

    def add(self, a):
        self.data_store[a] = True
