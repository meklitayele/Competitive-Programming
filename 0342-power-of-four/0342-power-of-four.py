class Solution:
    def isPowerOfFour(self, n: int) -> bool:

       # recursivelly divide by 4 if n == 4 then true if n < 4 false
        def calc(num):
            if num < 4 :
                return False
            elif num == 4:
                return True
            else:
                return calc(num/4)
        if n == 1:
            return True
        else:
            return calc(n)
    