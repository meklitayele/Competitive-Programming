class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.val = 0

class Tri:
    def __init__(self):
        self.root = TrieNode()
    def insertNode(self,word,num):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr.val += num
            curr = curr.children[ch]
        curr.val += num
        curr.is_end = True
        
class MapSum:

    def __init__(self):
        self.start = Tri()
        self.store = {}

    def insert(self, key: str, val: int) -> None:
        prev = self.store.get(key,0)
        change = val - prev
        self.store[key] = val

        curr = self.start
        curr.insertNode(key,change)
        
    def sum(self, prefix: str) -> int:
        curr = self.start.root
        for ch in prefix:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        return curr.val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)