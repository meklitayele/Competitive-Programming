class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)
        for start , end , direction in shifts:
            if direction == 0:
                prefix[start] -= 1
                if end + 1 < len(prefix):
                    prefix[end+1] += 1
            if direction == 1:
                prefix[start] += 1
                if end + 1 < len(prefix):
                    prefix[end+1] -= 1
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        
        res = []
        for i in range(len(s)):
            res.append(ord('a') + (ord(s[i]) - ord('a')+ prefix[i]) % 26 )


        return "".join(chr(i) for i in res)
     

        
        

        
                