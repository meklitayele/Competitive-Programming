class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        rich = defaultdict(list)
        indegree = [0] * n

        for x , y in richer:
            rich[x].append(y)
            indegree[y] += 1
        
        deq = deque()
        res = [i for i in range(n)]
        for i in range(n):
            if indegree[i] == 0:
                deq.append(i)

        while deq:
            node = deq.popleft()
            for n in rich[node]:
                if quiet[res[node]] < quiet[res[n]]:
                    res[n] = res[node]
                indegree[n] -= 1
                if indegree[n] == 0:
                    deq.append(n)
        return res
