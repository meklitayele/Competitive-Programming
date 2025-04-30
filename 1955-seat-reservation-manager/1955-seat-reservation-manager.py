class SeatManager:
    
    def __init__(self, n: int):
        self.n = n
        self.seats = [(i+1) for i in range(n)]
        # heapq.heapify(seats)
    def reserve(self) -> int:
        return heapq.heappop(self.seats)
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)