class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(2*n):
            curr = nums[i%n]
            while stack and curr > nums[stack[-1]]:
                ans[stack.pop()] = curr
            stack.append(i%n)
        
        
        
        return (ans)

            


        