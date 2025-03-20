class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(index,store):
            if len(store) == n:
                ans.append(store[:])
                return 

            for j in nums:
                if j not in store:
                    store.append(j)
                    backtrack(j+1,store)
                    store.pop()
        backtrack(0,[])
        return ans

        
        