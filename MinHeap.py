
# Implementation of a MinHeap using an list

class MinHeap:
    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.elements = [None for _ in range(size)]

    def get_left_child(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.elements[self.get_left_child(index)]

    def right_child(self, index):
        return self.elements[self.get_right_child(index)]

    def parent(self, index):
        return self.elements[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        tmp = self.elements[index_one]
        self.elements[index_one] = self.elements[index_two]
        self.elements[index_two] = tmp 

    def check_capacity(self):
        # if we have reached capacity, copy over the elements to a larger array
        if self.size == self.capacity:
            items = self.elements
            self.capacity *= 2
            self.elements = [None for _ in range(self.capacity)]

            for k,v in enumerate(items):
                self.elements[k] = v

    def peek(self):
        #return the root element (smallest)
        if self.size == 0:
            return None

        return self.elements[0]

    def poll(self):
        if self.size == 0:
            return None
        
        item = self.elements[0]
        self.elements[0] = self.elements[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self, item):
        self.check_capacity()
        self.elements[self.size] = item
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.elements[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapifyDown(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child(index)

            if self.elements[index] < self.elements[smaller_child_index]:
                break

            self.swap(index, smaller_child_index)

            index = smaller_child_index
