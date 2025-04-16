class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n , m = len(isWater) , len(isWater[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        matrix = [[-1] * m for _ in range(n)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        deq = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    deq.append((i,j,0))
                    matrix[i][j] = 0

        while deq:
            r , c , height = deq.popleft()
            for dx , dy in directions:
                newx , newy = r + dx , c + dy
                if inbound(newx,newy) and matrix[newx][newy] == -1:
                    matrix[newx][newy] = height + 1
                    deq.append((newx,newy,height+1))
        return matrix



