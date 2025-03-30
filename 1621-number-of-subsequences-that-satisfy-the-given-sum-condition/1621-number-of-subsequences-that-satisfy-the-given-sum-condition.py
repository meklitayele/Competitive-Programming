class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left , right = 0 , len(nums)-1
        count = 0
        MOD = pow(10,9) + 7
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count += pow(2,right - left,MOD)
                left += 1
            else:
                right -= 1
        return count % MOD