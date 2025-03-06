class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        # print(points)

        left = points[0][0]
        right = points[0][1]
        count = 1


        for i in range(1,n):
            if points[i][0] <= right:
                left = min(points[i][0],left)
                right = min(right,points[i][1]) 
                # print(left)
                # print(right)
            else:
                count += 1
                left = points[i][0]
                right = points[i][1]
                # print(count)
        return count
        
                







        

        