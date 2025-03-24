class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(index,store):
            if len(store) == n:
                val = ''.join(store)
                if n == 1:
                    ans.append(val)
                else: 
                    if '1' in val and '00' not in val:
                        ans.append(val)
                return
            for j in '01':
                store.append(j)
                backtrack(index+1,store)
                store.pop()

        backtrack(0,[])
        return ans

        