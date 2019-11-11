class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        #rows = len(array)/len (array[0])
        columns = len(array[0])

        row = 0
        column = columns - 1

        while (row < len(array) and column >= 0):
            if array[row][column] == target:
                return True
            elif array[row][column] < target:
                row += 1
            else:
                column -= 1
        return False
