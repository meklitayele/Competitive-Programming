class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        def dfs(r,c):
            for dx , dy in directions:
                newX , newY = dx + r , dy + c
                if inbound(newX,newY) and grid[newX][newY] == '1':
                    grid[newX][newY] = '0'
                    dfs(newX,newY)


        island = 0
        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)
        return island