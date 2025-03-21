class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def backtrack(index,store):
            if sum(store) == target:
                ans.append(store[:])
                return 
            for j in range(index,n):
                if sum(store) < target:
                    store.append(candidates[j])
                    backtrack(j,store)
                    store.pop()
        backtrack(0,[])
        return ans








        