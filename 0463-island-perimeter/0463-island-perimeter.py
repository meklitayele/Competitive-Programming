class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        
        def dfs(r , c):
            count = 0
            for dx , dy in directions:
                newX , newY = dx + r, dy + c
                if inbound(newX,newY) and grid[newX][newY] == 1:
                    count += 1    
            return count

        row , col = len(grid) , len(grid[0])
        pm = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    pm += 4 - dfs(i,j)
        return pm



        