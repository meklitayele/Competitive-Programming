class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def calc(num):
            while num > 1:
                num /= 2
            if num == 1:
                return True
            else:
                return False
        
        if calc(n):
            return True
        else:
            return False


            

            


        