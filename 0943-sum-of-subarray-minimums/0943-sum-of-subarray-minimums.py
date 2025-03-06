class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [1] * n
        stack = [] 

        for i in range(n):
            count = 1
            while stack and arr[stack[-1]] > arr[i]:
                count += left[stack[-1]]
                stack.pop()
            left[i] = count
            stack.append(i)
        
        right = [1] * n
        stack = [] 
        for i in range(n-1,-1,-1):
            count = 1
            while stack and arr[stack[-1]] >= arr[i]:
                count += right[stack[-1]]
                stack.pop()

            right[i] = count
            stack.append(i)
        
        ans = 0
        mod = 10**9 + 7
        for i in range(n):
            ans += arr[i] * left[i] * right[i]
            ans %= mod
        return ans




        # print(left)
        # print(right)





            



        