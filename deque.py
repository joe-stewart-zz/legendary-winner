class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)

if __name__ == '__main__':
    d = Deque()
    d.addFront(13)
    d.addRear(42)
    d.removeFront()
    n = d.removeRear()
    print(n)
    s = d.size()
    print(s)
    e = d.isEmpty()
    print(e)
