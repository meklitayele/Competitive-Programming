class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        n = len(self.stack)
        x =  self.stack[-1]
        self.newStack = []
        for i in range(n-1):
            self.newStack.append(self.stack[i])
        self.stack = []
        self.stack = self.newStack
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minval = float('inf')
        n = len(self.stack)
        for i in range(n):
            if self.stack[i] < minval:
                minval = self.stack[i]

        return minval
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()