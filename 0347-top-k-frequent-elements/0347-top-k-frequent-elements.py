class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for i in range(len(nums)):
            store[nums[i]] += 1
        val= list(store.items())
        val = [(-count,num) for num , count in val]
        
        heapq.heapify(val)
        count = 0
        res = []
        while count < k:
            freq , num = heappop(val)
            res.append(num)
            count += 1
        return res

        



