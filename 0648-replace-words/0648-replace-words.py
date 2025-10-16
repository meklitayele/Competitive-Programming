class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Tri:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Tri()
        for word in dictionary:
            trie.insert(word)
        
        arr = [word for word in sentence.split(' ')]
        for idx , word in enumerate(arr):
            curr = trie.root
            cnt = 0

            for ch in word:
                if ch in curr.children :
                    curr = curr.children[ch]
                    cnt += 1
                    if curr.is_end == True:
                        arr[idx] = word[:cnt]
                        break
                else:
                    break
        return(' '.join(arr))
                


        