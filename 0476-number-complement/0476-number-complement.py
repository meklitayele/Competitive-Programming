class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        
        ans = []
        def calc(n):
            while n > 0:
                if (n & 1):
                    ans.append('0')
                else:
                    ans.append('1')
                n //= 2
            return ans
        answer = calc(num)
        answer =''.join(answer)
        s = len(answer)
        
        total = 0
        for i in range(s):
            total += pow(2,i) * int(answer[i])
        return total

       
        


