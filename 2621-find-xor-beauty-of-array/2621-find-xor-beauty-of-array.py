class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        #1.brute force
        # values = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             values = values ^ ((w)
        #             print(k," or ", j, " and ", i)     
        # return values
  
        ans = 0
        for num in nums:
            ans ^= num
        return ans

       


                
                
                

            