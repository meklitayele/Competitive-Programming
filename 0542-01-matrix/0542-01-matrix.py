class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n , m = len(mat) , len(mat[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m
        
        matrix = [[-1] * m for _ in range(n)]
        deq = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    matrix[i][j] = 0
                    deq.append((i,j,0))
        
        while deq:
            i , j , moves = deq.popleft()
            for dx , dy in directions:
                newx , newy = dx + i , dy + j
                if inbound(newx,newy) and matrix[newx][newy] == -1:
                    matrix[newx][newy] = moves + 1
                    deq.append((newx,newy,moves+1))
        return matrix
                
        



        
        