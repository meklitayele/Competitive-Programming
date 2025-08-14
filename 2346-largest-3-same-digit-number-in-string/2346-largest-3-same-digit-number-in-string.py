class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = float('-inf')
        n = len(num)
        left = 0 
        right = left + 2
        l , r = 0 , 0

        while right < n :
            word = num[left:right+1]
            if (word[0] == word[1] == word[2]) and int(word) > good:
                good = int(word)
                l , r = left , right
            right += 1
            left += 1

        return(num[l:r+1] if good != float('-inf') else '')
       