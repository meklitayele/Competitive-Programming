class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 5
        if n % 2 == 0:
            even = pow(5 , (n//2), MOD)
            odd = pow(4 , (n//2), MOD)
            res = (even * odd) % (10**9 + 7)
        else:
            odd = pow(4,n // 2,MOD) 
            even =pow(5,(n//2) + 1,MOD)
            res = ((odd  * even) % (10**9 + 7))
        return res



        