import random
from collections import deque, OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# print(pages)
# puree demand paging
def FIFO(pages, size):
    miss = 0
    queue = deque([], maxlen=size)
    for page in pages:
        if page in queue:
            continue
        else:
            queue.append(page)
            miss += 1
    return miss / len(pages)


def LRU(pages, size):
    miss = 0
    queue = LRUCache(size)
    for page in pages:
        if queue.get(page) == -1:
            miss += 1
            queue.put(page, True)
    return miss / len(pages)


num_of_pages_in_ram = 35
pages = [random.randint(1, num_of_pages_in_ram + 1) for _ in range(10000)]
# pages = [i % 26 for i in range(10000)]

print(FIFO(pages, num_of_pages_in_ram))
print(LRU(pages, num_of_pages_in_ram))
