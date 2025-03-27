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

        left , right = 0 , pow(10,18)
        while left + 1 < right:
            mid = (left + right)//2
            if valid(mid):
                right = mid
            else:
                left = mid
        return right

        
    