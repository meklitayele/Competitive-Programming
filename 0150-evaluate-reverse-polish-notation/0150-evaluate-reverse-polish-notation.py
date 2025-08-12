class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+','-','*','/']
        store = []
        for i in range(len(tokens)):
            curr = tokens[i]
            if curr not in op:
                store.append(int(curr))
            else:
                x = store.pop()
                y = store.pop()
                if curr == '+':
                    store.append(x+y)
                elif curr == '-':
                    store.append(y-x)
                elif curr == '*':
                    store.append(x*y)
                else:
                    store.append(y//x if y*x > 0 else -(-y//x))
        return store[-1]

        