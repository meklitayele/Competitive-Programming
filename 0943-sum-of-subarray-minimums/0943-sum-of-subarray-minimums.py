class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []

        left = [0] * n
        for i in range(n):
            count = 1
            curr = arr[i]
            while stack and curr < arr[stack[-1]]:
                count += left[stack[-1]]
                stack.pop()
            stack.append(i)
            left[i] = count
        
        stack = []
        right = [0] * n
        for i in range(n-1,-1,-1):
            count = 1
            curr = arr[i]
            while stack and curr <= arr[stack[-1]]:
                count += right[stack[-1]]
                stack.pop()

            right[i] = count
            stack.append(i)
         
        ans = 0
        for i in range(n):
            ans += arr[i] * right[i] * left[i]
        return ans % (10**9 + 7)

        







        
      


        # print(left)
        # print(right)





            



        