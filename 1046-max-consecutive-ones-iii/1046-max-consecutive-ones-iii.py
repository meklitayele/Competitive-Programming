class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        n = len(nums)
        length = 0

        for right in range(n):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count-=1
                length = max(length, right - left )
                
                left += 1

        return length


            
       
        return length