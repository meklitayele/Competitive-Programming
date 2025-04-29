class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        arrivals = [(times[i][0] , i) for i in range(n)]
        arrivals.sort()

        free = list(range(n))
        heapq.heapify(free)

        leaving = []
        for at , idx in arrivals:
            while leaving and leaving[0][0] <= at:
                heapq.heappush(free,heapq.heappop(leaving)[1])
            chair = heapq.heappop(free)
            if idx  == targetFriend:
                return chair
            heapq.heappush(leaving,(times[idx][1],chair))
        return -1
