class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        num = set()
        sums = 0
        curr = 0

        for end in range(n):
            if nums[end] not in num:
                curr += nums[end]
                num.add(nums[end])

                if end - left + 1 == k:
                    sums = max(sums,curr)
                    curr -= nums[left]
                    num.remove(nums[left])
                    left += 1
            else:
                while nums[left] != nums[end]:
                    curr -= nums[left]
                    num.remove(nums[left])
                    left += 1
                left += 1
        return sums
                




        