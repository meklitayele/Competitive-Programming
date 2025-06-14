class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left , maxLen , count = 0 , 0 , 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            maxLen = max(right-left+1,maxLen)
        return maxLen


        
                
       

            
       