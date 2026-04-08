# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val: # if both are lower than the current root
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val: # if both are greater than the current root
            return self.lowestCommonAncestor(root.right, p, q)
        return root

        return self.lowestCommonAncestor(root, p, q)