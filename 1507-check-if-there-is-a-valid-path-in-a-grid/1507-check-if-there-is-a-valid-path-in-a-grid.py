class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n , m = len(grid) , len(grid[0])
        parent = {i:i for i in range(n*m)}
        size = [1] * (n*m)

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            r1 , r2 = find(x) , find(y)
            if r1 != r2:
                if size[r1] > size[r2]:
                    size[r1] += size[r2]
                    parent[r2] = r1
                else:
                    size[r2] += size[r1]
                    parent[r1] = r2
        direction = {
            'left' : (0,-1),
            'right' : (0,1),
            'up': (-1,0),
            'down': (1,0) 
        }
        types = {
            1: ['left','right'],
            2: ['up','down'],
            3: ['left','down'],
            4: ['down','right'],
            5: ['left','up'],
            6: ['up','right']
        }
        opp = {
            'up' : 'down',
            'down' : 'up',
            'left' : 'right',
            'right' : 'left'
        }

        def inbound(r,c):
            return 0<=r<n and 0<=c<m

        for r in range(n):
            for c in range(m):
                cell = grid[r][c]
                for d in types[cell]:
                    dr , dc = direction[d]
                    nr , nc = r + dr , c + dc
                    if inbound(nr,nc):
                        neigh = grid[nr][nc]
                        if opp[d] in types[neigh]:
                            i1 = r * m + c
                            i2 = nr * m + nc
                            union(i1,i2)
        return find(0) == find(m*n-1)

                
