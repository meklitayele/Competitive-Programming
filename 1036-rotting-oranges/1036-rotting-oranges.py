class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deq = deque()
        n , m = len(grid) , len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    deq.append((i,j,0))

        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        total = 0
        while deq:
            i , j , time = deq.popleft()
            for dx , dy in directions:
                newx , newy = dx + i , dy + j
                if inbound(newx,newy) and grid[newx][newy] == 1:
                    grid[newx][newy] = 2
                    total = max(total , time + 1)
                    deq.append((newx,newy,time + 1))
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return total
