class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def backtrack(index,store): 
            if len(store) <= n and store not in ans:
                ans.append(store[:])
            for j in range(index,n):
                if j < index and nums[j] == nums[j-1]:
                    continue
                store.append(nums[j])
                backtrack(j+1,store)
                store.pop()
        backtrack(0,[])
        return ans

         


        