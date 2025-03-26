class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(time):
            d = 0
            for rank in ranks:
                d += int(sqrt(time/rank))
            if d >= cars:
                return True
            else:
                return False
         
        left , right = 0 , min(ranks) * cars * cars
        res = right
        while left <= right:
            mid = (left + right) // 2  
            if valid(mid):
                right = mid - 1
                res = min(res,mid)
            else:
                left = mid + 1
        return res

