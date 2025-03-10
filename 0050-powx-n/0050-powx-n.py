class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def pow(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
                
            if n % 2 == 0:
                half = pow(x, n//2)
                return half * half
            else:
                half = pow(x, n//2)
                return half * half * x
        return pow(x,n) if  n > 0 else 1/pow(x,-n)

        

        