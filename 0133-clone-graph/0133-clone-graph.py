"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
# import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # b = deepcopy(node)
        # return b
        if not node:
            return node

        #the first copy of the first node
        visited = {node : Node(node.val)}
        deq = deque([node])
        while deq:
            currNode = deq.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val) #this creates its own copy
                    deq.append(neighbor)
                visited[currNode].neighbors.append(visited[neighbor])  #link all the nighbors

        return visited[node]



        