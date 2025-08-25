class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # diff = set(nums)
        # print(len(diff))
        j = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        return j
        
