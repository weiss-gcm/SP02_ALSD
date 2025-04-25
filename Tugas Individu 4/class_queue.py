class Queue:
    def __init__(self):
        self.items = []

    def Enqueue(self, item):
        self.items.append(item)

    def Dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def Peek(self):
        return self.items[0]

    def Size(self):
        return len(self.items)
