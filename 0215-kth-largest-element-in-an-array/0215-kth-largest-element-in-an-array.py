class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append(-nums[i])

        heapq.heapify(arr)
        count = 1
        while count < k:
            count += 1
            val = heapq.heappop(arr)
            
        val = -heapq.heappop(arr)
        return (val)




        



