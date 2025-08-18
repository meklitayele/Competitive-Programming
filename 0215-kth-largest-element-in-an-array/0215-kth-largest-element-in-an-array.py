class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = -1 * nums[i]

        heapq.heapify(nums)
        count = 1
        while count < k:
            count += 1
            val = heapq.heappop(nums)
            
        val = -heapq.heappop(nums)
        return (val)




        



