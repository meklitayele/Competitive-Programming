class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        #we can't use prefix and array
        #compute using sliding window
        left = 0
        maxL = 0
        start = 0 #to check if they share any common bit

        for right in range(len(nums)):
            while (start & nums[right]) != 0:  #move as long as i have a shared bit
                start ^= nums[left]
                left += 1
            start |= nums[right]  #set it with nums[right]
            maxL = max(maxL,right-left+1)
        return maxL
