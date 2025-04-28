class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -1 * piles[i]
        
        heapq.heapify(piles)
        count = 0
        while count < k:
            count += 1
            big = heapq.heappop(piles)
            half = (big//2)
            heapq.heappush(piles,half)

        return -(sum(piles))
            

            
        
        




        