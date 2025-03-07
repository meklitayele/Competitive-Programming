class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        n = len(s)
        m = len(t)

        for i in range(n):
            if stack1 and s[i] =='#':
                stack1.pop()
            elif s[i] != '#':
                stack1.append(s[i])
        print(stack1)
        for i in range(m):
            if stack2 and t[i] =='#':
                stack2.pop()
            elif t[i] != '#':
                stack2.append(t[i])
        print(stack2)
        return stack1 == stack2

       
        

        