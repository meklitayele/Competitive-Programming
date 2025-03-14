class Solution:
    def climbStairs(self, n: int) -> int:
        def calc(num):
            if num == 1:
                return 1
            if num == 2:
                return 2
            first , second = 1 , 2
            for i in range(3,num+1):
                first , second = second , first + second
            return second
        ans = calc(n)
        return ans
            




        