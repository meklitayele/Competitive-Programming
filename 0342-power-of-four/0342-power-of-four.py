class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def calc(n):
            if n < 4:
                return False
            elif n == 4:
                return True
            else:
                return calc(n/4)

        if n == 1:
            return True
        ans = calc(n)
        return ans
        