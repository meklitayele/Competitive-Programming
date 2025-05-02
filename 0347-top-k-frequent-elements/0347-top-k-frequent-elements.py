class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        store = list(store.items())
        store = [(count, num) for (num , count) in store]
        heapq.heapify(store)

        res = heapq.nlargest(k,store)
        return ([r[1] for r in res])
