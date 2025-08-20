class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums =sorted(set(nums)) 
        maxLen = 1
        streak = 1
        n = len(nums)
        prev = nums[0]
        for i in range(1,n):
            if prev + 1 == nums[i]:
                streak += 1
            else:
                maxLen = max(maxLen,streak)
                streak = 1
            prev = nums[i]
        maxLen = max(maxLen,streak)
        return maxLen