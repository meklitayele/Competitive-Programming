#dfs + trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root  = TrieNode()

    #node,word,idx
    def dfs(self,node,word,idx):
        n = len(word)
        #best case if we reached the end
        if idx == n:
            return node.is_end 

        char = word[idx]
        #we can use the dots as whatever letter
        if char == '.':
            for child in node.children.values():
                if self.dfs(child,word,idx+1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self.dfs(node.children[char],word,idx+1)
            

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node,word,0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)