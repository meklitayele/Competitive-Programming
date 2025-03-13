class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n == 0 :
        #     return False
        # while n % 2 == 0:
        #     n //= 2

        # if n == 1:
        #     return True
        # else:
        #     return False
        def pow(curr):
            if curr == 0:
                return False
            val = curr
            while val % 2 ==0 :
                val //= 2
            curr = val

            if curr == 1:
                return True
            else:
                return False

        ans = pow(n)
        return ans
            

            


        