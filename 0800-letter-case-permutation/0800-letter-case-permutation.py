class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        index = []
        for i , ch in enumerate(s):
            if ch.isalpha():
                index.append(i)
                
        n = len(index)
        store = []
        for i in range(pow(2,n)):
            word = list(s)
            for j in range(n):
                if (i >> j) & 1:
                    word[index[j]] = word[index[j]].upper()
                else:
                    word[index[j]] = word[index[j]].lower()
            store.append(''.join(word))
        return store


