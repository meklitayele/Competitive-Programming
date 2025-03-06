class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res =defaultdict(lambda : -1)

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > nums2[stack[-1]]:
                index = stack.pop()
                res[nums2[index]] = curr
            stack.append(i)

        result = []
        for i in range(len(nums1)):
            result.append(res[nums1[i]])

        
        return result


            


        