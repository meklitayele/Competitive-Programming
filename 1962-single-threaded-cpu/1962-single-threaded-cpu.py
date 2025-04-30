class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        #sort based on arrival time , store the index too
        tasks = sorted([(t[0],t[1],idx) for idx , t in enumerate(tasks)])
        time = tasks[0][0]
        i = 0
        store = []
      

        while len(res) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(store,(tasks[i][1],tasks[i][2]))
                i += 1
            if store:
                times , idx = heapq.heappop(store)
                time += times
                res.append(idx)
            elif i<len(tasks):
                time = tasks[i][0]

        return res

