class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        mheap = [(0,0)]
        n = len(points)
        total = 0

        while mheap and len(visited) < n:
            cost , idx = heappop(mheap)
            if idx in visited:
                continue
            visited.add(idx)
            total += cost
            x1 , y1 = points[idx]

            for i in range(n):
                if i not in visited:
                    x2 , y2 = points[i]
                    diff = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(mheap,(diff,i))
                 

        return total

        