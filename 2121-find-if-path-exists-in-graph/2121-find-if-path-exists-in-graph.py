class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        store = defaultdict(list)
        for u , v in edges:
            store[u].append(v)
            store[v].append(u)
        
        deq = deque([source])
        visited = set()
        while deq:
            curr = deq.popleft()
            for neigh in store[curr]:
                if neigh == destination:
                    return True
                if neigh not in visited:
                    deq.append(neigh)
                    visited.add(neigh)
                
            
        return False

        


        