class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        def calc(num):
            # print(num)
            if num == 3:
                return True
            elif num < 3:
                return False
            else:
                return calc(num/3)
        ans = calc(n)
        return ans
       
        