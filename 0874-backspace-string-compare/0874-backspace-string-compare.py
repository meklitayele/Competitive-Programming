class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        n = len(s)
        m = len(t)

        for i in range(n):
            if s[i] != '#':
                stackS.append(s[i])
            elif stackS and s[i] == '#':
                stackS.pop()
        for i in range(m):
            if t[i] != '#':
                stackT.append(t[i])
            elif stackT and t[i] == '#':
                stackT.pop()
        return stackT == stackS
        

        