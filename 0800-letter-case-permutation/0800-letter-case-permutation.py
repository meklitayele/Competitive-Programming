class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #store the index of the letters
        index = [index for index , char in enumerate(s) if char.isalpha()]
        n = len(index)
        ans = []

        for i in range(1<<n):
            word = list(s)
            for j in range(n):
                if (i >> j ) & 1:
                    word[index[j]] = word[index[j]].upper()
                else:
                    word[index[j]] = word[index[j]].lower()
            ans.append(''.join(word))
        return ans
