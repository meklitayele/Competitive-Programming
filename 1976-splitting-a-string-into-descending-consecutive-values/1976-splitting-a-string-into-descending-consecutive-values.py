class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def backtrack(index,prev):
            if index == n:
                return True
            for j in range(index,n):
                val = int(s[index:j+1])
                if val + 1 == prev and backtrack(j+1,val):
                    return True
            return False
        
        for i in range(n-1):
            val = int(s[:i+1])
            if backtrack(i+1,val):
                return True
        return False



