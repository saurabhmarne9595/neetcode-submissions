class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = []
        for i in range(n):
            tempPath = []
            for j in range(m):
                if j == m-1 or i == n-1:
                    tempPath.append(1)
                else:
                    tempPath.append(0)
            path.append(tempPath)
            
        for i in range(n-2, -1, -1):
            for j in range(m-2,-1,-1):
                path[i][j] =  path[i][j+1] + path[i+1][j]

        return path[0][0]