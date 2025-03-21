class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(idx,store,index):
            if len(store) == n and store not in ans:
                ans.append(store[:])
                return

            for i , num in enumerate(nums):
                if i not in index:
                    store.append(num)
                    index.append(i)
                    backtrack(0,store,index)
                    store.pop()
                    index.pop()
        backtrack(0,[],[])
        return ans