from node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

if __name__ == '__main__':
    mylist = UnorderedList()
    e = mylist.isEmpty()
    print(e)
    mylist.add(13)
    s = mylist.size()
    print(s)
    i = mylist.search(13)
    print(i)
    mylist.add(42)
    mylist.add(99)
    mylist.remove(42)
    print(mylist.search(13))
    print(mylist.search(99))
    print(mylist.size())
