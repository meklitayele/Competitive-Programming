class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0] , t[1],idx) for idx , t in enumerate (tasks)])
        time = tasks[0][0]
        store = []
        i = 0 

        while len(res) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(store,(tasks[i][1],tasks[i][2])) # this sorts it by processing time 
                i += 1
            if store:
                pt , idx = heappop(store)
                time += pt
                res.append(idx)
            elif i < len(tasks):
                time = tasks[i][0]
        return res

            


        
        