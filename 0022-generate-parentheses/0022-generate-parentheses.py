class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def calc(store,opn,close):
            if opn < n:
                store.append('(')
                calc(store,opn+1,close)
                store.pop()
            if close < opn:
                store.append(')')
                calc(store,opn,close+1)
                store.pop()
    
            if opn == close == n:
                ans.append(''.join(store))
        
        calc([],0,0)
        return ans

        

            
