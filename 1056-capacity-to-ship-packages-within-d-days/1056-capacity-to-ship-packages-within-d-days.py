class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(w):
            load = 0
            d = 1
            for weight in weights:
                if load + weight <= w:
                    load += weight 
                else:
                    d += 1
                    load = weight
            return True if d <= days else False

        left , right = max(weights),sum(weights) 
        while left  <= right:
            mid = (left + right)//2
            if valid(mid):
                curr = mid
                right = mid - 1
            else:
                left = mid + 1
        return curr