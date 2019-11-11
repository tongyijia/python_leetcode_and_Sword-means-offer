# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        res = sums = 3
        for i in range(number - 2):
            res = sums + 1
            sums += res
        return res
