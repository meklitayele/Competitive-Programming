class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        for i in range(n):
            stones[i] = -1*stones[i]
        heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                val = y - x
                heapq.heappush(stones,-val)
        return (-stones[0] if stones else 0)
                


