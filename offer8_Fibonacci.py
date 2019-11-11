# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        res = [1, 1]
        for i in range(n - 2):
            res.append(res[-1] + res[-2])
        return res[-1]
