class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower,-num)
        heapq.heappush(self.upper, -heappop(self.lower))
        
        if len(self.lower) < len(self.upper):
            heapq.heappush(self.lower,-heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return  (-self.lower[0] + self.upper[0])/ 2
            

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()