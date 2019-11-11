class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 0: return ""
        if len(s) == 1: return s

        m = len(s)
        map_table = [[0 for i in range(m)] for i in range(m)]
        max_l = 0
        res = []

        for i in range(m):
            map_table[i][i] = 1

        for i in range(m - 1):
            if s[i] == s[i+1]:
                map_table[i][i + 1] = 1
                map_table[i+1][i] = 1


        for i in range(m-1, -1, -1):
            for j in range(i, m):
                if i != j:
                    if map_table[i + 1][j - 1] == 1 and s[i] == s[j]:
                        map_table[i][j] = 1
                        map_table[j][i] = 1

        for i in  range(m):
            for j in range(m):
                if map_table[i][j] == 1:
                    tmp = abs(i - j) + 1
                    if tmp > max_l:
                        max_l = tmp
                        res = [i,j]

        return s[res[0]: res[1] + 1]
