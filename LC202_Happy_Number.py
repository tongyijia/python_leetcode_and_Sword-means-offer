class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def helper(n):
            res = 0
            while n >= 10:
                i = n % 10
                res += i * i
                n = n // 10
            res += n * n
            return res

        hash_table = {}
        tmp = n
        while tmp != 1:
            #print(tmp)
            if hash_table.has_key(tmp):
                return False
            else:
                hash_table[tmp] = 1
                tmp = helper(tmp)
        return True
