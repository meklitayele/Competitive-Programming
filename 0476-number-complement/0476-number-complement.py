class Solution:
    def findComplement(self, num: int) -> int:
        n = num.bit_length()
        ans = (1 << n) - 1
        print(ans)
        return ans ^ num