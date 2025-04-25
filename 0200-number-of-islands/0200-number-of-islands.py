class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        count = 0

        
        def bfs(x,y):
            deq = deque()
            deq.append((x,y))
            grid[x][y] = 0
            while deq:
                x , y = deq.popleft()
                for dx , dy in directions:
                    newx , newy = x + dx , y + dy
                    if inbound(newx,newy) and grid[newx][newy] == '1':
                        grid[newx][newy] = '0'
                        deq.append((newx,newy))
        
        n , m = len(grid) , len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i,j)
        return count
