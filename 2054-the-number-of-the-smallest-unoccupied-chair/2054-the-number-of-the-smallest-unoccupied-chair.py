class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        chairs = [i for i in range(n)]
        heapq.heapify(chairs)

        occupied = []
        times = sorted([t[0],t[1],idx] for idx , t in enumerate(times))
        for at , lt , idx in times:
            while occupied and occupied[0][0] <= at:
                heapq.heappush(chairs,heappop(occupied)[1])
            ch =  heappop(chairs)
            if idx == targetFriend:
                return ch
            heapq.heappush(occupied, [lt , ch])
            
        



        