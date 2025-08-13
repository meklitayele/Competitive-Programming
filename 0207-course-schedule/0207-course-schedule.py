class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        total = []
        store = defaultdict(list)
        degree =  [0] * numCourses
        for x , y in prerequisites:
            store[x].append(y)
            degree[y] += 1
        
        deq = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                deq.append(i)

        while deq:
            node = deq.popleft()
            total.append(node)
            for n in store[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    deq.append(n)
        ans = len(total) == numCourses
        return ans
                


