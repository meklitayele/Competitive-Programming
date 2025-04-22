class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        elements = set()
        curr , maxs = 0 , 0
        for end in range(len(nums)):
            if nums[end] not in elements:
                elements.add(nums[end])
                curr += nums[end]

                if end - start + 1 == k:
                    maxs = max(maxs , curr)
                    curr -= nums[start]
                    elements.remove(nums[start])
                    start += 1
            else:
                while nums[end] != nums[start]:
                    elements.remove(nums[start])
                    curr -= nums[start]
                    start += 1
                start += 1
        return maxs

                    