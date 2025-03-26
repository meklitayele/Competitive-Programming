class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        store = [capacity[i] - rocks[i] for i in range(len(capacity))]
        count = 0
        store.sort()
        for val in store:
            if val <= additionalRocks:
                additionalRocks -= val
                count += 1
            else:
                break
        return count 