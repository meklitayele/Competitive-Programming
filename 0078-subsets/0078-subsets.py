class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # the number of possible subsets
        n = len(nums)
        res = []
        for i in range(pow(2,n)):
            temp = []
            for j in range(i):
                if (i >> j) & 1:
                    temp.append(nums[j])
            res.append(temp)
        return res



       


