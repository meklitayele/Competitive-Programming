class Solution:
    def validPalindrome(self, s: str) -> bool:
        #delete at mose one okay
        left , right = 0 , len(s)-1
        while left < right:
            if s[left] != s[right]:
                if s[left:right][::-1] == s[left:right]:
                    return True
                elif  s[left+1:right+1][::-1] == s[left+1:right+1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True

       