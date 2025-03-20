class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(index,store,idx):
            if len(store) == n and store not in ans:
                ans.append(store[:])
                return 

            for i,num in enumerate(nums):
                if i not in idx:
                    store.append(num)
                    idx.append(i)
                    backtrack(i+1,store,idx)
                    store.pop()
                    idx.pop()
        backtrack(0,[],[])
        return ans


        