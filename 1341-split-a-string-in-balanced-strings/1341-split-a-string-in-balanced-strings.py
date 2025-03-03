class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        n = len(s)
        sums = 0
        for i in range(n):
            if s[i] == 'R':
                sums += 1
            elif s[i] =='L':
                sums -= 1
            
            if sums == 0:
                count += 1
        
        return count



        