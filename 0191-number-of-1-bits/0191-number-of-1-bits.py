class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        def calc(num):
            nonlocal count
            while num > 0 :
                if (num & 1):
                    count += 1
                num //= 2
        calc(n)
        return count
