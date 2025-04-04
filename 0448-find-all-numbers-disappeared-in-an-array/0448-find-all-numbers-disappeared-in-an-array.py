class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i , n = 0 , len(nums)
        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[pos] , nums[i] = nums[i] , nums[pos]
            else:
                i += 1
        # print(nums)
        ans = []
        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(i + 1)
        return ans
                