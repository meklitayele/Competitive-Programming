class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(s[i])
            else:
                val = stack.pop()
                if val == '(':
                    if stack and str(stack[-1]).isdigit():
                        stack[-1] += 1
                    else:
                        stack.append(1)     
                elif str(val).isdigit():
                    val2 = stack.pop()
                    if stack and str(stack[-1]).isdigit():
                        stack[-1] += 2*val
                    else:
                        stack.append(2*val)
        return stack[0]

        