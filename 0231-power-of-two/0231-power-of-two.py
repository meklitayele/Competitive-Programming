class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def calc(n):
            if n < 2:
                return False
            elif n == 2:
                return True
            else:
                return calc(n/2)
        if n == 1:
            return True
        ans = calc(n)
        return ans
            

            


        