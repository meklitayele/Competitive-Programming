class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def valid(force):
            count = 1
            prev = position[0]
            i = 1
            while i < len(position):
                if(position[i]-prev) >= force:
                    count += 1
                    prev= position[i]
                i += 1
            return True if count >= m else False

        left , right = 1, max(position)
        while left + 1 < right:
            mid = (left + right)//2
            if valid(mid):
                left = mid 
            else:
                right = mid 
        return left
       