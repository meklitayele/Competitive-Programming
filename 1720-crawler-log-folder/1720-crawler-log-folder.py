class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for ch in logs:
            if ch == "../" and stack :
                stack.pop()
            elif ch[0] != ".":
                stack.append(ch)
        return len(stack)