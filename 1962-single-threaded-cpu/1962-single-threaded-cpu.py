class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []

        #sort with arrival time and store index
        tasks = sorted([(t[0],t[1],idx) for idx , t in enumerate(tasks)])
        time = tasks[0][0]
        store = [] #heap with processing time
        i = 0
        
        #iterate till we cover all tasks
        while len(res) < len(tasks):
            #push everytask whose arrival time is less or equal to the current time
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(store,(tasks[i][1],tasks[i][2])) #proccesing and idx
                i += 1
            if store:
                pt , idx = heapq.heappop(store)
                time += pt
                res.append(idx)
            elif i < len(tasks):
                time = tasks[i][0]
        return res


