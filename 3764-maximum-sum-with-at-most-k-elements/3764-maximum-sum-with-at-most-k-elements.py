class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        array = []
        for idx , v in enumerate(grid):
            array.extend([-vals , idx] for vals in v)
        
        heapq.heapify(array)
        
         
        count = 0
        sums = 0
        while count < k:
            val = heappop(array)
            if limits[val[1]] > 0:
                sums += -(val[0])
                limits[val[1]] -= 1
                count += 1
        return sums
            

        

            
