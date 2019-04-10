import collections


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.cache = collections.OrderedDict()

    """
  Retrieves the value associated with the given key. Also needs to move the key-value pair to the top of the order such that the pair is considered most-recently used. Returns the value associated with the key or None if the key-value pair doesn't exist in the cache.
  """

    def get(self, key):
        # attempt to remove the value associated with the key
        try:
            # there might not be a value associated with the key
            # otherwise, store the value in a variable
            value = self.cache.pop(key)
            # re-add the key-value pair in order to reset the ordering
            # this will set this key-value pair as the newest element
            self.cache[key] = value

            # return the value
            return value
        except KeyError:
            # if there isn't return None
            return None

    """
  Adds the given key-value pair to the cache. The newly-added pair should be considered the most-recently used entry in the cache. If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.
  """

    def set(self, key, value):
        # attempt to fetch the key value associated with the key
        try:
            self.cache.pop(key)
        # if it isn't in the cache, we need to go ahead and add it
        except KeyError:
            # check to see if the cache is at its max capacity
            if len(self.cache) >= self.limit:
                # if it is, remove the least-recently used key-value pair
                self.cache
        # add the key-value pair to the cache
