class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area1 = 0 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def inbound(r,c):
            return 0 <=r<len(grid) and 0 <=c<len(grid[0])
            
        
        def dfs(r,c):
            grid[r][c] = 0
            area = 1
            for dx , dy in directions:
                newX , newY = dx + r , dy + c
                if inbound(newX,newY) and grid[newX][newY] == 1:
                    area += dfs(newX,newY)
            return area

        

        row , col = len(grid) , len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area1 = max(area1,dfs(i,j))
                    
        return area1