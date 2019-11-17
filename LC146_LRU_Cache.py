from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.table = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        self.table.move_to_end(key)
        return self.table[key]

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table.move_to_end(key)
        self.table[key] = value
        if len(self.table) > self.capacity:
            self.table.popitem(last = False)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
