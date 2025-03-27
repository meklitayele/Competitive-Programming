class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def valid(force):
            prev = position[0]
            count = 1
            i = 1
            while i < len(position):
                if(position[i] - prev) >= force:
                    count += 1
                    prev = position[i]
                i += 1
            return count >= m

        left , right = 1 , max(position)
        ans = 0
        while left <= right:
            mid = (left+right)//2
            if valid(mid):
                ans = max(mid,ans)
                left = mid + 1
            else:
                right = mid - 1
        return ans










       