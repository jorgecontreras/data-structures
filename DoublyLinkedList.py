

class DoublyLinkedBase:
    """A base class providing a doubly linked list implementation"""

    class _Node:
        """Class for storing a doubly linked node"""
        __slots__ = '_element', '_prev', '_next' #streamline memory

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        # return the number of elements in the list
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        """Add element between two existing nodes and return new node"""
        new_node = self._Node(element, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node 
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Remove node and return value removed"""
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


#TESTS

#create empty list
print('\n[Create empty list]')
airports = DoublyLinkedBase()
print('size: ' + str(len(airports)))
print('is empty? ', end='')
print(airports.is_empty())

#insert element
print('\n[Insert element]')
prv = airports._header
nxt = airports._trailer
airports._insert_between(5, prv, nxt)
print('size: ' + str(len(airports)))
print('is empty? ', end='')
print(airports.is_empty())

#remove element
print('\n[Remove element]')
rem = airports._Node(5, prv, nxt)
airports._delete_node(rem)
print('size: ' + str(len(airports)))
print('is empty? ', end='')
print(airports.is_empty())