class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        ans = 0
        sums = 0

        for i in range(32):
            bitA = (a >> i) & 1
            bitB = (b >> i) & 1
            sums = bitA ^ bitB ^ carry
            carry = (bitA & bitB) | (bitA & carry) | (bitB & carry)
            ans |= (sums << i)

        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans



