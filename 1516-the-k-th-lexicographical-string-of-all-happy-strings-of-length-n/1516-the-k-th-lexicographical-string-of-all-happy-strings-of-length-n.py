class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def backtrack(index , store):
            if len(store) == n:
                val = ''.join(store)
                if len(val) >= 2:
                    if 'aa' not in val  and 'bb'  not in val and 'cc'  not in val:
                        ans.append(val)
                else:
                    ans.append(val)
                return 

            for j in 'abc':
                store.append(j)
                backtrack(index+1,store)
                store.pop()
        backtrack(0,[])
        print(ans)
        if len(ans) < k:
            return ''
        else:
            return ans[k-1]

        