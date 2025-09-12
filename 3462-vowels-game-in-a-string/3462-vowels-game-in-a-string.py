class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = ['a','e','i','o','u']
        for char in s:
            if char.lower() in vowel:
                return True
        return False
            

        

        