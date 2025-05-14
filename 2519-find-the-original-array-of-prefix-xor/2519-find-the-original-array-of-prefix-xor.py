class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        res = [pref[0]]
        for i in range(1,n):
            res.append(pref[i] ^ pref[i-1])
        return res