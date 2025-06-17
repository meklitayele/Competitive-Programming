class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n , m = len(a) , len(b)
        c1 , c2 = 0 , 0
        sumA , sumB = 0 , 0

        for i in range(n-1,-1,-1):
            sumA += int(a[i]) * pow(2,c1) 
            c1 += 1
        
        for i in range(m-1,-1,-1):
            sumB += int(b[i]) * pow(2,c2)
            c2 += 1
         
        val = sumA + sumB
        return ((str(bin(val)))[2:])


        

    


        
      
