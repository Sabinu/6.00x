__author__ = 'Sabinu'


class Queue(object):
    """
    FIFO = first-in-fist-out

    """
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if not self.items:
            raise ValueError
        else:
            return self.items.pop(0)

q = Queue()
#q.remove()
q.insert(1)
q.insert(2)
print q.items
q.remove()
print q.items