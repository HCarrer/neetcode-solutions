"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def clone(node):
            if node in cloned:
                return cloned[node]

            newNode = Node(node.val)
            cloned[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(clone(neighbor))

            return newNode

        clonedNodes = clone(node) if node else None

        return clonedNodes