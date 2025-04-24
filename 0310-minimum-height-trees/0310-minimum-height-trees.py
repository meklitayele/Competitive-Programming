class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        indegree = [0] * n
        store = defaultdict(list)
        for x , y in edges:
            store[x].append(y)
            store[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        
        deq = deque()
        for num in range(n):
            if indegree[num] == 1:
                deq.append(num)

        leaf = n
        while leaf > 2:
            s = len(deq)
            leaf -= s
            for _ in range(s):
                node = deq.popleft()
                for n in store[node]:
                    indegree[n] -= 1
                    if indegree[n] == 1:
                        deq.append(n)
        return list(deq)
           

