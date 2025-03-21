class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def backtrack(index,store):
            if sum(store) == target:
                ans.append(store[:])
                return 
            for j in range(index,n):
                if sum(store) < target:
                    if j > index and candidates[j] == candidates[j-1]:
                        continue
                    store.append(candidates[j])
                    backtrack(j+1,store)
                    store.pop()

        backtrack(0,[])
        return ans