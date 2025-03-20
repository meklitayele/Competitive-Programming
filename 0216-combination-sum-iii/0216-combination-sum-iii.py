class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        values = [1,2,3,4,5,6,7,8,9]
        ans = []
        def backtrack(index,store):
            if len(store) == k:
                if sum(store) == n:
                    ans.append(store[:])
                    return
                

            for j in range(index,9):
                store.append(values[j])
                backtrack(j+1,store)
                if store:
                    store.pop()
                # store.pop()

        backtrack(0,[])
        return ans

