# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            
            if p.val < node.val and q.val < node.val: # if both are lower than the current node
                return dfs(node.left)
            if p.val > node.val and q.val > node.val: # if both are greater than the current node
                return dfs(node.right)
            return node

        return dfs(root)