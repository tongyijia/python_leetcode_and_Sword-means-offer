class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return

        direct = [(0,1),(0,-1),(-1,0),(1,0)]
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            board[i][j] = 'B'
            for x,y in direct:
                tmp_x = i + x
                tmp_y = j + y
                if 0 <= tmp_x < m and 0 <= tmp_y < n and board[tmp_x][tmp_y] == 'O':
                    dfs(tmp_x, tmp_y)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m-1][i] == 'O':
                dfs(m-1,i)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
