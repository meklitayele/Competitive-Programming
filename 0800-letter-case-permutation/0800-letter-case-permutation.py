class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = []
        index = []

        #store the index and letter for easier access
        for i in range(len(s)):
            if s[i].isalpha():
                index.append(i)
            letters.append(s[i])

        n =  len(index)
        # 00 01 10 11
        res = []
        for i in range(1<<n):
            word = letters[:]
            for j in range(n):
                if ((1 <<  j) & i):
                    word[index[j]] = word[index[j]].upper()
                else:
                    word[index[j]] = word[index[j]].lower()

            res.append(''.join(word))
        return res
