class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size = defaultdict(int)
        parent = defaultdict(list)
        cols = defaultdict(list)
        rows = defaultdict(list)

        for i , j in stones:
            cols[j].append((i,j))
            rows[i].append((i,j))
            size[(i,j)] += 1
            parent[(i,j)] = (i,j)
    
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            r1 , r2 = find(x) , find(y)
            if r1 == r2:
                return False
            if r1 != r2:
                if size[r1] > size[r2]:
                    size[r2] += size[r1]
                    parent[r2] = r1
                else:
                    size[r1] += size[r2]
                    parent[r1] = r2
            return True

        n , m = len(stones) , len(stones[0])             
        edge = 0
        for  val in rows.values():
            first = val[0]
            for v in val[1:]:
                if union(first,v):
                    edge += 1
        for  val in cols.values():
            first = val[0]
            for v in val[1:]:
                if union(first,v):
                    edge += 1
        return edge

        
        

        

        

        
        

                    



