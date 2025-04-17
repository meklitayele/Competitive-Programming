class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len(grid[0])
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        deq = deque()
        deq.append((0,0,1))
        grid[0][0] = 2

       
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        def inbound(r,c):
            return 0<=r<n and 0<=c<m
       
        while deq:
            r , c , moves = deq.popleft()
            if r == n - 1 and c == m - 1:
                    return moves
            for dx , dy in directions:
                newx , newy = dx + r , dy + c
                if inbound(newx,newy) and grid[newx][newy] == 0:
                    deq.append((newx,newy,moves+1))
                    grid[newx][newy] = 2
                
        return -1





        
        