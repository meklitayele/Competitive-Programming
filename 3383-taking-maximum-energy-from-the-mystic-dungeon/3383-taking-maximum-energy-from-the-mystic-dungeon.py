class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = {}
        def calc(idx):
            if idx >= n:
                return 0
            if idx in dp:
                return dp[idx]
            
            dp[idx] = energy[idx] + calc(idx + k)
            return dp[idx]

        total = float('-inf')
        for i in range(n):
            total = max(total , calc(i))
            
        return (total)
