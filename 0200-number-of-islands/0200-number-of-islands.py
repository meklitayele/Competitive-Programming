class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        deq = deque()
        n , m = len(grid) , len(grid[0])
        def inbound(x,y): 
            return 0 <= x < n and 0 <= y < m

        def dfs(nx,ny):
            for x , y in directions:
                newX , newY = x + nx , y + ny
                if inbound(newX,newY) and grid[newX][newY] == '1':
                    grid[newX][newY] = '0'
                    dfs(newX,newY)
        
        count = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x,y)
                    
        return count
                
