class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        total = 0
        
        def bfs(x,y):
            deq = deque()
            deq.append((x,y))
            grid[x][y] = '0'
            while deq:
                x , y  = deq.popleft()
                for dx , dy in directions:
                    newx , newy = x + dx , y + dy
                    if inbound(newx,newy) and grid[newx][newy] == '1':
                        grid[newx][newy] = '0'
                        deq.append((newx,newy))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    total += 1
                    bfs(i,j)
        return total

            
            
