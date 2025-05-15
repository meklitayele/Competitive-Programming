class Solution:
    def hammingWeight(self, n: int) -> int:
        def cnt(num):
            return bin(num).count('1')
        return cnt(n)