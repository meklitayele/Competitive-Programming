class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -heappop(stones)
            s2 = -heappop(stones)
            if s1 != s2:
                diff = s1 - s2
                heapq.heappush(stones,-diff)
        return -stones[0] if stones else 0