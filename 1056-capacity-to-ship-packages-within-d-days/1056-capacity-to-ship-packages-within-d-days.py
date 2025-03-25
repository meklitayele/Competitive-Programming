class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(cap):
            load = 0
            day = 1
            for i in range(len(weights)):
                if weights[i] + load > cap:
                    load = weights[i]
                    day += 1
                else:
                    load += weights[i]
            if day > days:
                return False
            else:
                return True

        left , right = max(weights) , sum(weights)
        result = right
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                result = min(result,mid)
                right = mid - 1   
            else:
                left = mid + 1
        return result
        