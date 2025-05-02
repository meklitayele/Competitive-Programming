class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        for i in range(min(k,len(nums1))):
            res.append((nums1[i] + nums2[0],i,0))
        heapq.heapify(res)

        ans = []
        while len(ans) < k:
            sums , i , j = heappop(res)
            ans.append([nums1[i],nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(res,(nums1[i]+nums2[j+1],i,j+1))
                # print(res)

        return ans


        

        

