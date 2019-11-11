class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def count_cell(x, y):
            points = [
                (x-1, y-1),
                (x-1, y),
                (x-1, y+1),
                (x, y-1),
                (x, y+1),
                (x+1, y-1),
                (x+1, y),
                (x+1, y+1),
            ]
            return sum((board[i][j] & 1) for i, j in points if 0 <= i < max_x and 0 <= j < max_y)

        if not board:
            return board

        max_x, max_y = len(board), len(board[0])

         # 计算周围细胞数目，并储存
        for i in range(max_x):
            for j in range(max_y):
                count = count_cell(i, j)
                count <<= 1
                board[i][j] |= count

        for i in range(max_x):
            for j in range(max_y):
                count = board[i][j] >> 1   # 右移一位，取出周围细胞数目
                board[i][j] &= 1   # 重新设置原先细胞状态
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1
        return board
