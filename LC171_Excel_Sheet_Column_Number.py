class Solution:
    def titleToNumber(self, s: str) -> int:

        res = 0
        for i in range(0, len(s)):
            if ord(s[i]) < 65 or ord(s[i]) > 90:
                return False
            elif i == len(s)-1:
                res += ord(s[i]) - 65 + 1
            else:
                res += 26 ** (len(s) - i - 1) * (ord(s[i]) - 65 + 1)

        return res
