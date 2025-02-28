class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        minPrefix = maxPrefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            minPrefix = min(prefix,minPrefix)
            maxPrefix =max(prefix, maxPrefix)
       

        return maxPrefix - minPrefix