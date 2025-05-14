class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        count = 0
        def calc(num):
            nonlocal count
            while num > 0:
                if (num & 1):
                    count += 1
                num //= 2
        calc(ans)
        return count
        