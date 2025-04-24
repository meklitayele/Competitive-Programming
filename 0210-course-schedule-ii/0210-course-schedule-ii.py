class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        indegree = [0] * numCourses
        for x , y in prerequisites:
            store[y].append(x)
            indegree[x] += 1
        deq = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                deq.append(n)
        
        res = []
        while deq:
            node = deq.popleft()
            res.append(node)
            for n in store[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    deq.append(n)
        return res if len(res) == numCourses else []


        
        