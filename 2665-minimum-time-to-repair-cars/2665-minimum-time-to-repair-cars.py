class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(time):
            total = 0
            for rank in ranks:
                total += int(sqrt(time/rank))
            return True if total >= cars else False
        left , right = 0 , pow(10,18)
        curr = right
        while left <= right:
            mid = (left + right)//2 
            if valid(mid):
                right = mid - 1
                curr = mid
            else:
                left = mid + 1
        return curr
       