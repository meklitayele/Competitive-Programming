class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chair = [i for i in range(len(times))]
        order = [(idx,f) for idx , f in enumerate(times)]
        order.sort(key= lambda x : x[1][0],reverse = True)

        heapq.heapify(chair)
        leave = []
        heapq.heapify(leave)
        time = 0

        while True:
            time += 1
            while leave and time == leave[0][0]:
                l , c = heappop(leave)
                heappush(chair,c)
            if order[-1][1][0] == time:
                ch = heappop(chair)
                idx , tup = order.pop()
                if idx == targetFriend:
                    return ch
                heappush(leave,(tup[1],ch))