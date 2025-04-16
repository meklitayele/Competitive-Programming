class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        n , m = len(grid) , len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        deq = deque()
        for  i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    deq.append((i,j,0))

        total = 0
        if not deq or len(deq) == n*m:
            return -1
        while deq:
            i , j , moves = deq.popleft()
            for dx , dy in directions:
                newx , newy = dx + i , dy + j
                if inbound(newx,newy) and grid[newx][newy] == 0:
                    grid[newx][newy] = 2
                    total = max(total,moves+1)
                    deq.append((newx,newy,moves+1))
        return total     


        
        