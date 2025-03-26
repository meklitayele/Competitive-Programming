class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l , r = 0 , 0
        res = []
        n , m = len(nums1),len(nums2)
        nums1.sort()
        nums2.sort()
        while l < n and r < m:
            if nums1[l] == nums2[r]:
                if nums2[r] not in res:
                    res.append(nums2[r])
                r += 1
                l += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return res
        