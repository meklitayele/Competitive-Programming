class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0 , x
        while left <= right:
            mid = (left + right)//2
            v = mid * mid
            if v == x:
                return mid
            elif v < x:
                left = mid + 1
            else:
                right = mid - 1
        return right



        