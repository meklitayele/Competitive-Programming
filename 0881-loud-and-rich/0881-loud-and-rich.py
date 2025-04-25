class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        store = defaultdict(list)
        n = len(quiet)
        indegree = [0] * n
        for x , y in richer:
            store[x].append(y)
            indegree[y] += 1
        
        res = [i for i in range(n)]
        deq = deque()
        for i in range(n):
            if indegree[i] == 0:
                deq.append(i)
        
       
        while deq:
            node = deq.popleft()
            for n in store[node]:
                if quiet[res[n]] > quiet[res[node]]:
                    res[n] = res[node]
                indegree[n] -= 1
                if indegree[n] == 0:
                    deq.append(n)
        return res

        
