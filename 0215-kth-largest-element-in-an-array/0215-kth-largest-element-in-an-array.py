class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        heapq.heapify(nums)
        count = 1
        while count < k:
            heappop(nums)
            count += 1
        return -(nums[0])
