class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i , n = 0 , len(nums)

        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[pos] , nums[i]  = nums[i] , nums[pos]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return [nums[i] , i + 1]
        
