class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        streak = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                streak += 1
                count += streak
            else:
                streak = 0

        
        return (count)

        