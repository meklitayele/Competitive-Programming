class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        store = defaultdict(list)
        indegree = [0] * n
        for x , y in edges:
            store[x].append(y)
            store[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        size = n
        deq = deque()
        for i in range(n):
            if indegree[i] == 1:
                deq.append(i)

        while size > 2:
            s = len(deq)
            size -= s
            for _ in range(s):
                node = deq.popleft()
                for n in store[node]:
                    indegree[n] -= 1
                    if indegree[n] == 1:
                        deq.append(n)
        return list(deq)




