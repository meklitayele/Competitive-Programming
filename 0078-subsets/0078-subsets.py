class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(1<<n):
            store = []
            for j in range(n):
                if (i >> j) & 1:
                    store.append(nums[j])
            ans.append(store)
            
        return ans





        return


       


