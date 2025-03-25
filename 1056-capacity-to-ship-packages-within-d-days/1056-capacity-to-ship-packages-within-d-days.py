class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(num):
            load = 0
            day = 1
            for weight in weights:
                if weight + load <= num:
                    load += weight
                else:
                    day += 1
                    load = weight
            if day > days:
                return False
            else:
                return True
        left , right = max(weights) , sum(weights)
        curr = right
        while left <= right:
            mid = (left + right)//2
            if valid(mid):
                curr = min(curr,mid)
                right = mid - 1
            else:
                left = mid + 1
        return curr
            


