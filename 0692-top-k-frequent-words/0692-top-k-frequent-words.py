class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        store = defaultdict(int)
        for word in words:
            store[word] -= 1
        store = list(store.items())
        store = [(count,word) for (word,count) in store]
        heapq.heapify(store)
        
        count = 0
        res = []
        while count < k:
            count += 1
            ans = heappop(store)
            res.append(ans[1])
        return res

        


        