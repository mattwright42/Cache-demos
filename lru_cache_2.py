from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        # storage is the hash table
        self.storage = {}
        # our dll keeps track of the order of elements in the cache
        self.order = DoublyLinkedList()

    """
  Retrieves the value associated with the given key. Also needs to move the key-value pair to the top of the order such that the pair is considered most-recently used. Returns the value associated with the key or None if the key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # check to see if the key is in the ht
        if key in self.storage:
            # if it is, store it in a variable
            node = self.storage[key]
            # move the node to the tail of the list
            self.order.move_to_end(node)
            # return the value in the node
            return node.value[1]
        # else, it isn't in the ht
        else:
            # return None
            return None

    """
  Adds the given key-value pair to the cache. The newly-added pair should be considered the most-recently used entry in the cache. If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.
  """

    def set(self, key, value):
        # check to see if the key already exists in the ht
        if key in self.storage:
            # if it does, store it in a variable
            node = self.storage[key]
            # overwrite the key's value
            node.value = (key, value)
            # move this key-value pair to the end of the dll, to signify that it's now the newest element.
            self.order.move_to_end(node)
        # if it isn't in the ht
        else:
            # check to see if the cache is already at max capacity
            if len(self.storage) == self.limit:
                # delete the ht entry associated with the value being stored in the head of the linked list
                del self.storage[self.order.head.value[0]]
                # if it is, remove the least-recently accessed element
                self.order.remove_from_head()
            # add the key-value pair to the dll
            self.order.add_to_tail((key, value))
            # add the key-value pair to the ht
            self.storage[key] = self.order.tail
