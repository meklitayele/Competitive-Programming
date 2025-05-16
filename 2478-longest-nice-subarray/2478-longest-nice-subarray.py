class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # in prefix and always use ~0 or -1 
        #we don't need prefix and
        # ans = ~0
        # arr = []
        # for n in nums:
        #     ans &= n
        #     arr.append(ans)
        # print(arr)

        left = 0
        start = 0
        maxL = 0
        for right in range(len(nums)):
            #while there's a shared bit move left pointer 
            while (start & nums[right]) != 0:
                start ^= nums[left]
                left += 1
            start |= nums[right]
            maxL = max(maxL , right-left+1)
        return (maxL)



        