class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        deq = deque()
        n , m = len(mat) , len(mat[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(x,y):
            return 0<=x<n and 0<=y<m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    deq.append((i,j,0))
                else:
                    mat[i][j] = -1
        while deq:
            x , y , dis = deq.popleft()
            for dx , dy in directions:
                newx , newy = dx + x , dy + y
                if inbound(newx,newy) and mat[newx][newy] == -1:
                    mat[newx][newy] = dis + 1
                    deq.append((newx,newy,dis+1))
        return mat

