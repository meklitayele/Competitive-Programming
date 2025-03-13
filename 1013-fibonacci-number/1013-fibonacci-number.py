class Solution:
    def fib(self, n: int) -> int:
        def calc(n):
            if n == 1:
                return 1
            if n == 0:
                return 0

            return(calc(n-1) + calc(n-2))
        
        ans = calc(n)
        return ans
        




       

        