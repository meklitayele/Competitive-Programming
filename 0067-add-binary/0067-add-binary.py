class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = 0
        a = a[::-1]
        newA ,newB = 0 , 0
        for i in range(len(a)):
            newA += int(a[i]) * pow(2,i)

        b = b[::-1]
        for i in range(len(b)):
            newB += int(b[i]) * pow(2,i)
        
        
        value = newA + newB
        return (bin(value)[2:])
        
    

        
      
