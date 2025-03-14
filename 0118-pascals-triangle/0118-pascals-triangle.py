class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @cache
        def calc(r,c):
            if r == c:
                return 1
            if c == 0:
                return 1
            else:
                return calc(r-1,c-1) + calc(r-1,c)

        ans = [[calc(r,c) for c in range(r+1)]for r in range(numRows)]
        return ans
        