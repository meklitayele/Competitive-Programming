class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #1. brute force approach
        # store = defaultdict(int)
        # for num in nums:
        #     store[num] += 1
        # for key , value in store.items():
        #     if value == 1:
        #         return key

        #2. bit manipulation
        #count unbalanced ones occ % 3
        #this doesn't handle negative numbers
        ans = 0
        for i in range(32):
            ones = 0
            for num in nums:
                if num < 0:
                    num = num & (2**32-1)  #two's complement for negative numbers
                ones += (num  >> i) & 1
            ones %= 3
            ans |= (ones << i)

        if ans >= 2**31:
            ans -= 2**32

        return ans



        