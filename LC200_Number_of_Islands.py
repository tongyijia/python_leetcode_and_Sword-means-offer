class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:return 0

        m = len(grid)
        n = len(grid[0])
        table = [[0 for i in range(n + 2)] for j in range(m + 2)]
        count = 0

        grid.append(["0" for i in range(n)] )
        grid.insert(0, ["0" for i in range(n)])

        for i in range(m + 2):
            grid[i].append(0)
            grid[i].insert(0,"0")
        #print(table)

        def dfs(i,j,table,grid):
            table[i][j] = 1
            if grid[i + 1][j] == "1" and table[i + 1][j] == 0:
                dfs(i+1,j,table,grid)

            if grid[i][j + 1] == "1" and table[i][j + 1] == 0:
                dfs(i,j+1,table,grid)

            if grid[i - 1][j] == "1" and table[i - 1][j] == 0:
                dfs(i-1,j,table,grid)

            if grid[i][j - 1] == "1" and table[i][j - 1] == 0:
                dfs(i,j-1,table,grid)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if table[i][j] == 0:
                    table[i][j] = 1
                    #print(table)
                    if grid[i][j] == "1":
                        count += 1
                        dfs(i,j,table,grid)
        return count
