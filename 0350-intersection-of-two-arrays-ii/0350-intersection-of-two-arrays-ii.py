class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        store = Counter(nums2)

        for num in nums1 :
            if num in nums2 and store[num]:
                res.append(num)
                store[num] -= 1
        return res
        