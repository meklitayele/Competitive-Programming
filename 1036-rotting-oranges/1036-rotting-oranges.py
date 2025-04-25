class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq = deque()
        n , m = len(grid) , len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    deq.append((i,j,0))

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(x,y):
            return 0<=x<n and 0<=y<m

        total = 0
        while deq:
            x , y , time = deq.popleft()
            for dx , dy in directions:
                newx , newy = x + dx , y + dy
                if inbound(newx , newy) and grid[newx][newy] == 1:
                    grid[newx][newy] = 2
                    total = max(total,time+1)
                    deq.append((newx,newy,time+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return total

            


            


    