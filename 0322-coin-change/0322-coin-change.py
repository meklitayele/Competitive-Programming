class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        #curr amount and number of coins
        #visited array to keep track of next amounts seen
        deq = deque([(0,0)])
        visited = set()

        while deq:
            currAmt , numCoin = deq.popleft()
            for coin in coins:
                nextAmt = currAmt + coin
                if nextAmt <= amount and nextAmt not in visited:
                    if nextAmt == amount:
                        return numCoin + 1
                    visited.add(nextAmt)
                    deq.append([nextAmt,numCoin+1])

    
        return -1

        
