class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)

        for i in range(1,n+1):
            #check for the half and if it's odd
            res[i] = res[i>>1] + (i & 1)
        return res
        


           


            


        