class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                ans += 8 * count[product]
                count[product] += 1

        return ans
        