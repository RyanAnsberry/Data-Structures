import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # We can use a DLL to easily and efficiently add and remove nodes from the tail and head.
        # self.storage = ?
            # Our chosen data structure (DLL)
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # check for empty queue, if so, return None
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()



    def len(self):
        return self.size