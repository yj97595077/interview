#!/usr/bin/python

'''
https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
'''

import sys
from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        cache = OrderedDict()
        self.cache = cache
        self.capacity = capacity

    def get(self, key):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            value = None

        return value

    def set(self, key, value):
        if self.cache.has_key(key):
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                self.cache[key] = value
            else:
                self.cache[key] = value

lru_cache = LRUCache(5)
lru_cache.set(1, 'a')
print lru_cache.cache
lru_cache.set(4, 'd')
print lru_cache.cache
lru_cache.set(3, 'c')
print lru_cache.cache
lru_cache.set(2, 'b')
print lru_cache.cache
print lru_cache.get(3)
print lru_cache.cache
print lru_cache.get(5)
print lru_cache.cache
lru_cache.set(6, 'f')
print lru_cache.cache
lru_cache.set(5, 'e')
print lru_cache.cache

