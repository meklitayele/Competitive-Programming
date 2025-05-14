class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(32):
            sums = sum((num>>i) & 1 for num in nums)
            count += sums * (n-sums)




        return count
