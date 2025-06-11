class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n , m = len(nums1) , len(nums2)
        if n % 2 == 0 and m % 2 == 0:
            return 0
        elif n % 2 != 0 and m % 2 != 0:
            start = 0
            for num in nums1:
                start ^= num
            for num in nums2:
                start ^= num
            return start
        elif n % 2 == 0:
            start = 0
            for num in nums1:
                start ^= num
            return start
        else:
            start = 0
            for num in nums2:
                start ^= num
            return start


       