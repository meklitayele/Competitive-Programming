class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def calc(store,index):
            if sum(store) == target:
                ans.append(store[:])
                return 
            if sum(store) > target:
                return 
            for i in range(index,n):
                store.append(candidates[i])
                calc(store,i)
                store.pop()
        calc([],0)
        return ans

       