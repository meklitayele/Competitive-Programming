class Solution:
    def calPoints(self, operations: List[str]) -> int:
        store = []
        for op in operations:
            if op == 'C':
                store.pop()
            elif op == '+':
                z = store[-1] + store[-2]
                store.append(z)
            elif op == 'D':
                x = store[-1]
                y = 2 * x
                store.append(y)
            else:
                store.append(int(op))
            print(store)
        return sum(store)


        