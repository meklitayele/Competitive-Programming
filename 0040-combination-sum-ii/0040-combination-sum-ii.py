class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        store = []
        def backtrack(index,s):
            if s == target:
                ans.append(store[::] )
                return
            if s>target:
                return 
            
            for j in range(index,n):
                if s < target:
                    if j > index and candidates[j] == candidates[j-1]:
                        continue
                    store.append(candidates[j])
                    s+=candidates[j]
                   
                    backtrack(j+1,s)
                    
                    s -= store.pop()
                    
        backtrack(0,0)
        return ans


        