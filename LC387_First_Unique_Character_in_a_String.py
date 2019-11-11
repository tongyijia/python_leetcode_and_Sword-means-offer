class Solution:
    def firstUniqChar(self, s: str) -> int:

        hash_table = dict()

        for i in s:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in range(len(s)):
            if s[i] in hash_table and hash_table[s[i]] == 1:
                return i
        return -1
