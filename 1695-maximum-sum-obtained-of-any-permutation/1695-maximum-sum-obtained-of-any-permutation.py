class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #because it's zero indexed we don't add 1
        prefix = [0] * len(nums)
        for start , end in requests:
            prefix[start] += 1
            if end + 1 < len(prefix):
                prefix[end+1] -= 1

        for i in range(1 , len(prefix)):
            prefix[i] += prefix[i-1]
        prefix.sort()
        nums.sort()

        ans = 0
        for i in range(len(prefix)):
            ans += (prefix[i] * nums[i]) % (10**9 + 7)
        return ans % (10**9 + 7)


       