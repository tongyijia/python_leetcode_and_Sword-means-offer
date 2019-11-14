class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        raw = set()
        columns = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    raw.add(i)
                    columns.add(j)
        for i in range(m):
            for j in range(n):
                if i in raw or j in columns:
                    matrix[i][j] = 0
