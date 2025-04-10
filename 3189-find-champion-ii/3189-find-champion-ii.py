class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        allWinner = [True] * n
        for winner,loser in edges:
            allWinner[loser] = False
        
        winnerCount = 0
        winner = -1
        for i in range(n):
            if allWinner[i]:
                winnerCount += 1
                winner = i
        if winnerCount == 1:
            return winner
        else:
            return -1

