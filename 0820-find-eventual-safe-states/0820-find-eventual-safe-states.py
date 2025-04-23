class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outgoing = [0] * len(graph)
        store = defaultdict(list)
        for n in range(len(graph)):
            outgoing[n] = len(graph[n])
            for v in graph[n]:
                store[v].append(n)
                
        
        terminal = deque()
        for n in range(len(graph)):
            if outgoing[n] == 0:
                terminal.append(n)
        
        res = []
        while terminal:
            node = terminal.popleft()
            res.append(node)
            for n in store[node]:
                outgoing[n] -= 1
                if outgoing[n] == 0:
                    terminal.append(n)
                    
        return sorted(res)
            


        




