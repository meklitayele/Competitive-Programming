class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        sums = 0
        carry = 0

        for i in range(32):
            num1 , num2 = (a >> i) & 1 , (b >> i) & 1
            sums = num1 ^ num2 ^ carry
            carry = (num1 & carry) | (num2 & carry) | (num1 & num2)
            ans |= (sums << i)
        
        if ans > 2**31:
            ans -= 2 ** 32

        return ans


