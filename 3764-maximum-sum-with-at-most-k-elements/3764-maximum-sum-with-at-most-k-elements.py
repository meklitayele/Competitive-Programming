class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        for g in grid:
            heapq.heapify(g)

        store = []
        for idx , val in enumerate(grid):
            store.extend([(-v,idx)  for v in val])
        heapq.heapify(store)

        res = []
        while len(res) < k:
            ans , idx = heapq.heappop(store)
            if limits[idx] == 0:
                continue
            else:
                limits[idx] -= 1
                res.append(-ans)
        return (sum(res))




        print(store)









        
