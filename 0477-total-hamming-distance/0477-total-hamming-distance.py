class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(32):
            ones = sum(((num>>i) & 1) for num in nums)
            zeros = n - ones
            count += ones * zeros



        return count