class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p = 0
        num = 2
        while pow(num,p) < n:
            p += 1 
        if pow(num,p) == n:
            return True
        else:
            return False

            

            


        