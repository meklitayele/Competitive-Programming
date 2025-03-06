class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * (len(nums2))

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > nums2[stack[-1]]:
                index = stack.pop()
                res[index] = curr
            stack.append(i)
        result = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            result.append(res[index])



        
        return (result)


            


        