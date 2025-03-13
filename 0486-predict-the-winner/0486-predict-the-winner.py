class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(nums,turn,i,j):
            if i > j:
                return 0
            if (turn):
                return max((nums[i] + play(nums,False,i+1,j)),(nums[j] + play(nums,False,i,j-1)))
            else:
                return min(play(nums,True,i+1,j),play(nums,True,i,j-1))
        
        total = 0
        for i in range(len(nums)):
            total += nums[i]
        player1 = play(nums,True,0,len(nums)-1)
        player2 = total - player1
        return player1 >= player2


       
                


        