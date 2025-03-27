class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(size):
            load = 0
            d = 1
            for weight in weights:
                if weight + load <= size:
                    load += weight
                else:
                    d += 1
                    load = weight
            if d > days:
                return False
            else:
                return True

        left , right = max(weights) , sum(weights) 
        curr = right
        while left <= right:
            mid = (left + right)//2
            if valid(mid):
                right = mid - 1
                curr = min(mid,curr)
            else:
                left = mid + 1
        return curr



