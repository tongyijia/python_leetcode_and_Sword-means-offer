class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        res = 0
        for i in s:
            if i == '1': res += 1

        return res  
