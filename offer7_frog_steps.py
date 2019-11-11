# -*- coding:utf-8 -*-
class Solution:
    #循环
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        steps = [1, 2]
        for i in range(number - 2):
            steps.append(steps[-1] + steps[-2])
        return steps[-1]
