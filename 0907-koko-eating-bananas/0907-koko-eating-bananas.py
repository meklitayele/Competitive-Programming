class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(amount):
            hour = 0
            for  pile in piles:
                hour += math.ceil(pile / amount)
            return hour <= h


        left , right = 1, max(piles)
        result = right
        while left <= right:
            mid = (left + right) //2
            if valid(mid):
                result = min(result,mid)
                right = mid -1
            else:
                left = mid + 1
        return result
        




