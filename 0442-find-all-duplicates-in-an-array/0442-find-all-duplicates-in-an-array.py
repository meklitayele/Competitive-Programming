class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        i ,  n = 0 , len(nums)
        while i < n:
            pos = nums[i] - 1
            if nums[i]!= nums[pos]:
                nums[pos] , nums[i] = nums[i] , nums[pos]
            else:
                i += 1
        
        # print(nums)
        res = []
        
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                res.append(nums[i])

        return res

        

        

       

        