class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        store = {0 : -1}
        ans  = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count -= 1
            else:
                count += 1
            
            if count in store:
                ans = max(ans,i-store[count])
            else:
                store[count] = i
        return ans
            







        