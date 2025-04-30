class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        
        store = list(store.items())
        store = [(count,num) for (num,count) in store]

        heapq.heapify(store)
        ans = heapq.nlargest(k,store)
        print(ans)
        return [x[1] for x in ans]
        
