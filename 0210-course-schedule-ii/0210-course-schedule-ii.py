class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        degree = [0] * numCourses
        store = defaultdict(list)
        deq = deque()
        degree = [0] * numCourses

        for x , y in prerequisites:
            degree[x] += 1
            store[y].append(x)

        for i in range(numCourses):
            if degree[i] == 0:
                deq.append(i)
        
        while deq:
            node = deq.popleft()
            ans.append(node)
            for n in store[node]:
                degree[n] -= 1
                if degree[n] == 0:
                    deq.append(n)
        
        return ans if len(ans) == numCourses else []
