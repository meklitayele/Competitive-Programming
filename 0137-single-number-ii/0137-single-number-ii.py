class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            count = 0
            for num in nums:
                if num < 0 :
                    num = num & (2 **32-1)
                if (num >> i) & 1:
                    count += 1
            ans |= (count % 3) << i

        
        if ans >= 2**31:
            ans -= 2 ** 32
        return ans

        