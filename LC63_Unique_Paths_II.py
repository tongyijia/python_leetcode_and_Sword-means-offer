class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0: return 0
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0

        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(1,m):
            if dp[i-1][0] == 1 and obstacleGrid[i-1][0] != 1:
                dp[i][0] = 1
        for j in range(1,n):
            if dp[0][j-1] == 1 and obstacleGrid[0][j-1] != 1:
                dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i-1][j] == 1 or dp[i-1][j] == 0:
                    from_up = 0
                else:
                    from_up = dp[i-1][j]
                if obstacleGrid[i][j-1] == 1 or dp[i][j-1] == 0:
                    from_left = 0
                else:
                    from_left = dp[i][j-1]
                dp[i][j] = from_up + from_left
        return dp[-1][-1] if obstacleGrid[-1][-1] == 0 else 0
