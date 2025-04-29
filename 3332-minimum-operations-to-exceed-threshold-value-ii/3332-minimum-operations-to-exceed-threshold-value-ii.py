class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        while len(nums) > 1 and nums[0] < k:
            
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            ans = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums,ans)
            count += 1

        return count





        