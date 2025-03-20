class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        n = len(candidates)
        candidates.sort()
        def backtrack(index,store):
            if sum(store) == target:
                ans.add(tuple(sorted(store[:]) ))
                return
            
            for j in range(index,n):
                if sum(store) < target:
                    store.append(candidates[j])
                    if j > index and candidates[j] == candidates[j-1]:
                        store.pop()
                        continue
                    backtrack(j+1,store)
                    store.pop()
                    
        backtrack(0,[])
        return [list(num) for num in ans]


        