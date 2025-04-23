class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        indegree = [0] * numCourses
       
        for a , b in prerequisites:
            store[b].append(a)
            indegree[a] += 1

        deq = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                deq.append(n)
        
        visited = []
        while deq:
            course = deq.popleft()
            visited.append(course)
            for n in store[course]:
                indegree[n] = max(0,indegree[n]-1)
                if indegree[n] == 0:
                    deq.append(n)
        return visited if len(visited) == numCourses else []


            
