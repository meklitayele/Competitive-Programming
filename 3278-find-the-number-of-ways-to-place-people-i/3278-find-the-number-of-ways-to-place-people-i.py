class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x :(x[0],-x[1]) )
        ans = 0
        n = len(points)
        for i in range(n-1):
            x , y = points[i]
            lower = -1
            for j in range(i+1,n):
                if lower < points[j][1] <= y:
                    lower = points[j][1]
                    ans += 1
                # if lower == y:
                #     break
        return ans