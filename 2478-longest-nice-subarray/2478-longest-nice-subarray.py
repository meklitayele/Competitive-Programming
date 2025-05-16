class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        left = 0
        maxL = 0
        n = len(nums)
        start = 0

        for right in range(n):
            while (start & nums[right]) != 0:
                start ^= nums[left]
                left += 1
            start |= nums[right]
            maxL = max(maxL,right-left+1)
        return maxL
            
