class Solution:
    directs = [(1,0),(-1,0),(0,1),(0,-1)]
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        if m == 0: return False
        used = [[0 for i in range(n)] for i in range(m)]


        def backtrack(i, j, word):
            if len(word) == 0:
                return True
            for direct in self.directs:
                cur_i = i + direct[0]
                cur_j = j + direct[1]

                if 0 <= cur_i < m and 0 <= cur_j < n and board[cur_i][cur_j] == word[0]:
                    if used[cur_i][cur_j] == 1:
                        continue
                    used[cur_i][cur_j] = 1
                    if backtrack(cur_i, cur_j, word[1:]) == True:
                        return True
                    else:
                        used[cur_i][cur_j] = 0
            return False
            

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = 1
                    if backtrack(i, j, word[1:]) == True:
                        return True
                    else:
                        used[i][j] = 0
        return False
