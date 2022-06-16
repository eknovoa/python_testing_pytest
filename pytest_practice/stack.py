class Stack:
    def __init__(self):
        self._storage = []          # internal storage inside stack data structure

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item

