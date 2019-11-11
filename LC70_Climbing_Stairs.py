class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: return 1
        if n == 2: return 2

        dp = [1,2]
        for i in range(3,n+1):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
