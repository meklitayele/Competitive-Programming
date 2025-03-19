class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(index,store):
            if len(store) == k:
                ans.append(store[:])
            for j in range(index,n+1):
                store.append(j)
                backtrack(j+1,store)
                store.pop()
        backtrack(1,[])
        return ans
       
        