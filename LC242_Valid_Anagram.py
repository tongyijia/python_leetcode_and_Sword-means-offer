class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) : return False

        hash_table = {}
        for i in s:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in t:
            if i in hash_table:
                hash_table[i] -= 1
                if hash_table[i] == 0:
                    del hash_table[i]
            else:
                return False

        if len(hash_table) == 0:
            return True
        else:
            return False
