class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        for i in range(32):
            bit = (n >> i) & 1
            val |= (bit << (31-i))
        return val