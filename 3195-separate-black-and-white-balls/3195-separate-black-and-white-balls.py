class Solution:
    def minimumSteps(self, s: str) -> int:
        black = 0
        white = 0

        for i in range(len(s)):
            if s[i] == '1':
                black += 1
            else:
                white += black
        return white

        


            




