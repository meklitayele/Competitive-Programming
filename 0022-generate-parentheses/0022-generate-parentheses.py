class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(opens,close,store):
            if len(store) == 2*n:
                val = ''.join(store)
                ans.append(val)
                return
            if opens < n :
                store.append('(')
                backtrack(opens+1,close,store)
                store.pop()
            if close < opens:
                store.append(')')
                backtrack(opens,close+1,store)
                store.pop()


            
        backtrack(0,0,[])
        return ans
        