from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.current_size = 0
        self.entries = DoublyLinkedList()
        self.dictionary = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if cache is empty
        if self.current_size == 0:
            return None
        # if key isn't in cache
        elif key not in self.dictionary:
            return None
        # if key is in cache
        else:
            # If node is already head, return it
            if self.entries.head.key == key:
                return self.dictionary[key]
            else:
                # moves key/value pair top (most recent)
                self.entries.move_to_front(key, self.dictionary[key])
                # retrieves value of given key
                return self.dictionary[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Check if key is already in dictionary
        if key in self.dictionary:
            # update existing entry
            self.dictionary[key] = value
            # Move it to the head if it isn't already
            if self.entries.head.key != key:
                self.entries.move_to_front(key, value)
        
        else:
            # Increase current size
            self.current_size += 1
            # Remove tail node if current size is bigger than limit
            if self.current_size > self.limit:
                self.entries.remove_from_tail()
                self.dictionary.pop(self.entries.tail.key)
                self.current_size -= 1
            # Add new entry node to head of DLL and add new entry to dictionary
            self.entries.add_to_head(key, value)
            self.dictionary[key] = value


