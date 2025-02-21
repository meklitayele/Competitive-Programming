class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        sums = 0
        ans = 0

        for i in range(len(nums)):
            sums += nums[i]
            rem = sums % k
            ans += store[rem]
            store[rem] += 1
        return ans

       