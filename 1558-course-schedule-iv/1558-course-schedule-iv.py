class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        store = defaultdict(list)
        indegree = [0] * numCourses
        for x , y in  prerequisites:
            store[x].append(y)
            indegree[y] += 1
        
        deq = deque()
        res = [[] for _ in range(numCourses)]
        for i in range(numCourses):
            if indegree[i] == 0 :
                deq.append(i)

        while deq:
            node = deq.popleft()
            for n in store[node]:
                res[n].append(node)
                res[n].extend(res[node])
                res[n] = list(sorted(set(res[n])))
                indegree[n] -= 1
                if indegree[n] == 0:
                    deq.append(n)
        

        ans = []     
        for x , y in queries:
            for i in res[y]:
                if i == x:
                    ans.append(True)
                    break
            else:
                ans.append(False)
        return ans





        