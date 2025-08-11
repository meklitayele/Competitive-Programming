class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        operators = ['+' , '-' , '/' , '*']
         
        stack = []
        for i in range(n):
            curr = tokens[i]
            if curr not in operators:
                stack.append(int(curr))
            else:
                x = stack.pop()
                y = stack.pop()
                if curr == '+':
                    stack.append(x+y)
                elif curr == '*':
                    stack.append(x*y)
                elif curr == '-':
                    stack.append(y-x)
                else:
                    ans =  y // x if y*x > 0 else -(-y//x)
                    stack.append(ans)
        return stack[-1]

        



        