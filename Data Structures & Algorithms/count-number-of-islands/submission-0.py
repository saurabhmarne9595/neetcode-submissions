class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        res = 0
        seen = set()
        def dfs(r,c):
            if((r,c) in seen or r < 0 or r >= ROWS or c <0 or c >= COLS or grid[r][c] =="0"):
                return 0
            seen.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            

        for i in range (ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in seen:
                    res+= 1
                    dfs(i, j)
        return res
