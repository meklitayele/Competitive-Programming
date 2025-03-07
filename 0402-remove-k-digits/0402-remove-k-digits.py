class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        n = len(num)
        length = n - k

        for i in range(n):
            while stack and num[i] < stack[-1] and k:
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        ans = "".join(stack[:length])
        return ans.lstrip('0') or '0'
        
            
        