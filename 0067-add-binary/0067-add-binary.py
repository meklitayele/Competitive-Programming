class Solution:
    def addBinary(self, a: str, b: str) -> str:
        newA = 0
        c = 0
        for i in range(len(a)-1,-1,-1):
            newA += pow(2,c) * int(a[i])
            c+= 1
        print(newA)
        
        newB = 0
        c = 0
        for i in range(len(b)-1,-1,-1):
            newB += pow(2,c) * int(b[i])
            c += 1
        
        return str(bin(newA+newB)[2:])

    


        
      
