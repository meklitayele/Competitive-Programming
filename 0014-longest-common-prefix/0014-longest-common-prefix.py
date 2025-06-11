class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min(strs,key=len)
        

        for i , s in enumerate(minLen):
            for ch in strs:
                if ch[i] != s:
                    return minLen[:i]
        return minLen
                
        



