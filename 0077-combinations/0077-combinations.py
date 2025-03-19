class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i , store):
            if len(store) == k:
                ans.append(store[:])
            for j in range(i+1,n+1):
                store.append(j)
                backtrack(j,store)
                store.pop()
        backtrack(0,[])
        return ans