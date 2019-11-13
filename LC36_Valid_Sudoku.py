class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        m = len(board)
        n = len(board[0])
        raws = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        cross = [{} for i in range(9)]

        for i in range(m):
            for j in range(n):
                k = board[i][j]
                if k != '.':
                    if k not in raws[i]:
                        raws[i][k] = 1
                    else:
                        return False
                    if k not in columns[j]:
                        columns[j][k] = 1
                    else:
                        return False
                    if k not in cross[(i // 3) * 3 + j // 3]:
                        cross[(i // 3) * 3 + j // 3][k] = 1
                    else:
                        return False

        return True
