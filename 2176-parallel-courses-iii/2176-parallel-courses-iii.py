class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        store = defaultdict(list)
        indegree = [0] * (n+1)
        for x , y in relations:
            store[x].append(y)
            indegree[y] += 1

        deq= deque()
        t = [0] * (n+1)
        for i in range(1,n+1):
            if indegree[i] == 0:
                deq.append(i)
                t[i] = time[i-1]
       
       
        while deq:
            node = deq.popleft()
            for v in store[node]:
                indegree[v] -= 1
                t[v] = max(t[v],time[v-1] + t[node])
                if indegree[v] == 0:
                    deq.append(v)
            
        return max(t)