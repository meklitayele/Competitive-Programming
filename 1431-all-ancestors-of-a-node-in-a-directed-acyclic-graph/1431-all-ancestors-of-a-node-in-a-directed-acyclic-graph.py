class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        store = defaultdict(list)
        indegree = [0] * n
        res = [[] for _ in range(n)]

        for x , y in edges:
            store[x].append(y)
            indegree[y] += 1

        deq = deque()
        for num in range(n):
            if indegree[num] == 0:
                deq.append(num)

        while deq:
            node = deq.popleft()
            for n in store[node]:
                res[n].extend(res[node])
                res[n].append(node)
                res[n] = list(sorted(set(res[n])))

                indegree[n] -= 1
                if indegree[n] == 0:
                    deq.append(n)
        return res

        