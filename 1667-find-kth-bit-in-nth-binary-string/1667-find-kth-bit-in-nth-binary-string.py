class Solution:
    def findKthBit(self, n: int, k: int) -> str: 
        def calc(n , k):
            if n == 1:
                return '0'

            length = (2 ** n) - 1
            mid = math.ceil(length / 2)

            if k == mid:
                return '1'
            elif k < mid:
                return calc(n-1,k)
            else:
                return '1' if  calc(n-1,length-k+1) == '0' else '0'
        ans = calc(n , k)
        return ans
        
                
            
        

          
            
        