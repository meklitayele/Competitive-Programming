class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l , r = 0 , 0
        n , m = len(nums1) , len(nums2)
        
        res = []
        while l < n and r < m:
            if nums1[l] == nums2[r]:
                res.append(nums2[r])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return res

        