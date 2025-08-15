"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        deq = deque([root])
        while deq:
            n = len(deq)
            node = None
            for _ in range(n):
                currNode = deq.popleft()
                currNode.next = node
                node = currNode
                if currNode.right:
                    deq.append(currNode.right)
                if currNode.left:
                    deq.append(currNode.left)
                
        return root
        