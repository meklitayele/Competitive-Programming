class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def calc(num):
            if num == 1:
                return 1
            if num == 2:
                return 2
            return calc(num-1) + calc(num-2)
        ans = calc(n)
        return ans
            




        