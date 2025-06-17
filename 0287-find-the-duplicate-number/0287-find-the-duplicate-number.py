class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = Counter(nums)
        for key , value in store.items():
            if value != 1:
                return key