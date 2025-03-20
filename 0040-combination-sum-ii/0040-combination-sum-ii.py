class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        store = []
        def backtrack(index,s):
            if s == target:
                ans.append(list(store) )
                return
            if s>target:
                return 
            
            for j in range(index,n):
                if s < target:
                    store.append(candidates[j])
                    s+=candidates[j]
                    if j > index and candidates[j] == candidates[j-1]:
                        
                        s -= store.pop()
                        continue
                    backtrack(j+1,s)
                    
                    s -= store.pop()
                    
        backtrack(0,0)
        return ans


        