class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def valid(h):
            count = 0
            for cite in citations:
                if cite >= h:
                    count += 1
            return count >= h
        left , right = 0 , max(citations)
        ans = float('-inf')
        while left <= right:
            mid = (left + right)//2
            if valid(mid):
                ans = max(ans,mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans

