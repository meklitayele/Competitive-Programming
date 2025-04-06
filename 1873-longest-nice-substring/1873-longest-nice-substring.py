class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <= 1:
            return ''

        store = defaultdict(int)
        for c in s:
            store[c] += 1

        i = 0 
        flag = False
        while i < len(s):
            if s[i].isupper()  and s[i].lower() in store.keys():
                pass
            elif s[i].islower() and s[i].upper() in store.keys():
                pass
            else:
                flag = True
                break
            i += 1
        if not flag:
            return s
        part1 = self.longestNiceSubstring(s[:i])
        part2 = self.longestNiceSubstring(s[i+1:])

        if len(part1) >= len(part2):
            return part1
        else:
            return part2
        
            
