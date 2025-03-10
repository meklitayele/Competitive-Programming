class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        happiness.sort()
        n = len(happiness)
        count = 1
        for i in range(n-1,-1,-1):
            if k==0:
                break
            if happiness[i] < 0:
                happiness[i] = 0
            total += happiness[i]
            k -= 1
            happiness[i-1] -= count
            count += 1
        return total
        

        