class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        store = []
        n = len(nums)
        for i in range(1<<n):
            soln = []
            for j in range(n):
                if (i >> j) & 1:
                    soln.append(nums[j])
            if sorted(soln) not in store:
                store.append(sorted(soln))
                ans.append(soln)
        
        return ans
