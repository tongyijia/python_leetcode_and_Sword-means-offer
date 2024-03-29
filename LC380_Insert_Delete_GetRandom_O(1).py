class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hash_table:
            return False
        else:
            self.hash_table[val] = 1
            return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hash_table:
            del self.hash_table[val]
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        k = random.randint(0,len(self.hash_table) - 1)
        return list(self.hash_table.keys())[k]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
