class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        n = len(graph)
        outdegree = [0] *n
        
        for i in range(n):
            for v in graph[i]:
                store[v].append(i)
                outdegree[i] += 1
        # print(store)
        # print(outdegree)

        deq = deque()
        for i in range(n):
            if outdegree[i] == 0:
                deq.append(i)

        res = []
        while deq:
            node = deq.popleft()
            res.append(node)
            for n in store[node]:
                outdegree[n] -= 1
                if outdegree[n] == 0:
                    deq.append(n)
        return sorted(res)

        

