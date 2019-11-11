class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        if s[::-1] == s:
            return True
        else:
            return False
