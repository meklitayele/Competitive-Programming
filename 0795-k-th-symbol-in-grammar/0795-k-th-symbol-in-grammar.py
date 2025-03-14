class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def calc(n,k):
            if n == 1:
                return 0
            length = 2 ** (n-1)
            mid = length / 2

            if k <= mid:
                return calc(n-1,k)
            else:
                return 1 - calc(n-1,k-mid)
        ans = calc(n,k)
        return ans
        
        


        
         

        







        