class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        queue = deque([('0000',0)])
        visited = set('0000')

        while queue:
            comb , moves = queue.popleft()
            if comb == target:
                return moves
            moves += 1

            for i in range(4):
                for d in [-1,1]:
                    num = (int(comb[i]) + d) % 10
                    newNum = comb[:i] + str(num) + comb[i+1:]
                    if newNum not in visited and newNum not in deadends:
                        visited.add(newNum)
                        queue.append((newNum,moves))
        return -1
        
                
                