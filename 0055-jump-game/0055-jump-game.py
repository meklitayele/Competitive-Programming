class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        maxStep = 0
        for i , num  in enumerate(nums):
            if  i + num >= n-1:
                return True
            elif num == 0 and maxStep <= i:
                return False
            maxStep = max(maxStep , i+num)



        # zero = defaultdict(list)
        # for i in range(n):
        #     if nums[i] == 0:
        #         zero[0].append(i)
        # # print(zero[0][0])
        
        # for i in range(n):
        #     if (i + nums[i]) > zero[0][0]:
        #         del zero[0][0]
        #         return True

        return False

        

        

        

            
        







        