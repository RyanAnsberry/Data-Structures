import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # We can use a DLL to easily and efficiently add and remove nodes from the head.
        # self.storage = ?
            # Our chosen data structure (DLL)
        self.storage = DoublyLinkedList()
        

    def push(self, value):
        self.storage.add_to_head(value)
        self.size +=1


    def pop(self):
        # check for empty stack, if so, return None
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
