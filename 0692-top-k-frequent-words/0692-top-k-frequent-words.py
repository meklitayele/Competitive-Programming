class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        store = defaultdict(int)
        for word in words:
            store[word] -= 1
        store = list(store.items())
        store = [(count,val) for (val,count) in store]
        heapq.heapify(store)

        ans = heapq.nsmallest(k,store)
        return [x[1] for x in ans]
        


        