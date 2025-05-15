class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num = x ^ y
        return bin(num).count('1')
        