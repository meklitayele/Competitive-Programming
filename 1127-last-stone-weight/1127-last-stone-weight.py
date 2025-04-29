class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)
        while len(stones) >= 2:
            num1 = -(heappop(stones))
            num2 = -(heappop(stones))
            if num1 == num2:
                continue
            else:
                ans = num1-num2
                heappush(stones,-ans)
        return -(stones[0]) if stones else 0

        