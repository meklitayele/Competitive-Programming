class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(speed):
            d = 0
            for pile in piles:
                d += math.ceil(pile / speed)
            if d <= h:
                return True
            else:
                return False

        left , right = 1 , max(piles)
        result = right
        while left <= right:
            mid = (left + right)//2
            if valid(mid):
                right = mid - 1
                result = min(result,mid)
            else:
                left = mid + 1
        return result
        
            
