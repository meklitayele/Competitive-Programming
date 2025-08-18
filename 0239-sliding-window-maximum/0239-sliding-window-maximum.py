class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        n = len(nums)
        for right in range(n):
            while dq and nums[right] > nums[dq[-1]]:
                dq.pop()

            dq.append(right)
            if dq[0] < right-k+1:
                dq.popleft()
            
            if right >= k-1:
                ans.append(nums[dq[0]])
                
        return (ans)

        