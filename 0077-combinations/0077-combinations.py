class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(index,store):
            if len(store) == k:
                ans.append(store[:])

            for j in range(index,n):
                store.append(j+1)
                backtrack(j+1,store)
                store.pop()
        backtrack(0,[])
        return ans