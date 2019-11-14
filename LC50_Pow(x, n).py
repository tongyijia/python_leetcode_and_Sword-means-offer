class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        judge = True
        if n < 0:
            n = abs(n)
            judge = False
        if n == 0:
            return 1
        final = 1
        while n > 0:
            if n % 2 == 0:
                x *= x
                n //= 2
            final *= x
            n -= 1
        return final if judge else 1/final
