class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        operators = ['/','*','+','-']
        stack = []
        for i in range(n):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '*':
                    res= a *b
                elif tokens[i] =='/':
                    res = b//a if b*a > 0  else -(-b//a)
                elif tokens[i] == '+':
                    res = a + b
                else:
                    res = b - a 
                stack.append(res)

        return stack[-1]
        



        