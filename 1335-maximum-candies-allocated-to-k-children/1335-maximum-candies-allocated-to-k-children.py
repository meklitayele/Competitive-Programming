class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(size):
            count = sum(candy//size for candy in candies)
            return count >= k
     
        if sum(candies) < k:
            return 0

        left , right = 1 , max(candies)
        curr = 0
        while left <= right:
            mid = (left + right)//2
            if valid(mid) :
                left = mid + 1
                curr = max(curr,mid)
            else:
                right = mid - 1
        return curr 