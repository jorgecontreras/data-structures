# Singly Linked Lists

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedListSimple:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    # This append is slow because it has to go over every item to find the last one (next=None)
    def appendSlow(self, data):
        """Add a new node to the end of the list O(n)"""
        node = Node(data)

        if self.tail == None:
            self.tail = node 
        else:
            current = self.tail
            while current.next:
                current = current.next 
            current.next = node 
        self.size += 1

    #This append is faster because we already know where the last one is
    def appendFast(self, data):
        """Add a new node to the end of the list, but faster O(1)"""
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size += 1

        
    def show(self):
        """Traverse the list printing its nodes"""
        current = self.tail
        while current:
            print ("[ data={} ][ next={} ]".format(current.data, current.next))
            current = current.next

    def size(self):
        return self.size

grocery = LinkedListSimple()
grocery.appendFast("ham")
grocery.appendFast("soda")
grocery.appendFast("mango")
grocery.appendFast("pear")
grocery.appendFast("lime")
grocery.appendFast("peanuts")

print(grocery.show())
print(grocery.size)