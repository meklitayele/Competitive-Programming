class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        store = defaultdict(int)
        for a , b in trust:
            store[a] -= 1
            store[b] += 1

        for i in range(1,n+1):
            if store[i] == n - 1:
                return i
        return -1

        
        
        print(s)

