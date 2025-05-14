class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # the number of possible subsets
        n = pow(2,len(nums))
        res = []

        for num in range(n):
            sub = []
            for i in range(num):
                if num & (1 << i):
                    sub.append(nums[i])
            res.append(sub)
        return res


       


