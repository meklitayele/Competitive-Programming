class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        values = Counter(nums)
        ans = []
        for key , value in values.items():
            if value == 2:
                ans.append(key)
        return ans

        