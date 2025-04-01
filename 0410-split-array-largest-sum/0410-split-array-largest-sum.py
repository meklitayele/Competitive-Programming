class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(total):
            parts = 1
            amount = 0
            for num in nums:
                if num + amount <= total:
                    amount += num
                else:
                    parts += 1
                    amount = num
            return True if parts <= k else False
        
        left , right = max(nums), sum(nums)
        curr = right
        while left  <= right:
            mid = (left + right) // 2
            if valid(mid):
                curr = mid
                right = mid - 1
            else:
                left = mid + 1
        return curr
    
            