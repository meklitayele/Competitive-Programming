class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def valid(radius):
            i , j = 0 , 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= radius:
                    i +=1
                else:
                    j += 1
            return i == len(houses)
        left , right = 0 , max(houses[-1],heaters[-1])
        curr = 0
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                curr = mid
                right = mid - 1 
            else:
                left = mid + 1
        return curr
