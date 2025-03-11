class Solution:
    def fib(self, n: int) -> int:
        def calc(num):
            if num == 0 :
                return 0
            if num == 1:
                return 1

            return calc(num-1) + calc(num-2)
        ans = calc(n)
        return ans

        