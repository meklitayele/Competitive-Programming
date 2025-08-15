class Solution:
    def numSquares(self, n: int) -> int:
        numbers = [] 
        i = 1
        while i * i <= n:
            numbers.append(i*i)
            i += 1
        # print(numbers)
        #start number and starting amount
        deq = deque([(0,0)])
        visited = set()
        while deq:
            prevAmt , numAmt = deq.popleft()
            for num in numbers:
                amount = prevAmt + num
                if amount <= n and amount not in visited:
                    if amount == n:
                        return numAmt + 1
                    visited.add(amount)
                    deq.append((amount , numAmt + 1))
        
                    
