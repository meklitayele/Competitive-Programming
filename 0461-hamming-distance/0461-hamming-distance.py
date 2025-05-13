class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        count = 0
        while ans > 0:
            if ans % 2 != 0:
                count += 1
            ans = ans // 2
        return count
        
        