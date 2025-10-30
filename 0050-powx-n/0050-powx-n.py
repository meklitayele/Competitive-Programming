class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        negative = n < 0
        n = abs(n)

        #while we still have the exponent
        while n > 0:
            #if we have a set bit
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        
        if negative:
            return 1 / result
        else:
            return result
            


            

        