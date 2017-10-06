class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, data):
        self.data = data
    def setNext(self, next):
        self.next = next

if __name__ == '__main__':
    n = Node(13)
    x = n.getData()
    print(x)
    n.setData(42)
    y = n.getData()
    print(y)
