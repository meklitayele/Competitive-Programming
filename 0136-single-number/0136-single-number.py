class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = 0
        for n in nums:
            start ^= n
        return start