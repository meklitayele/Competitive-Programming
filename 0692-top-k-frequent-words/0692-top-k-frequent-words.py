class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        store = defaultdict(int)
        for word in words:
            store[word] -= 1
        heap = list(store.items())
        heap = [(count,word) for word , count in heap]
        # print(heap)

        heapq.heapify(heap)
        res = []
        for _ in range(k):
            ans = heappop(heap)
            res.append(ans[1])
        return res
        




    
        

    
