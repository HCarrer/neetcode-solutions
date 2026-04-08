# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = float("-inf")

        def dfs(node, prevTotal):
            if not node:
                return False
            
            prevTotal += node.val
            if not node.left and not node.right:
                return prevTotal == targetSum

            return dfs(node.left, prevTotal) or dfs(node.right, prevTotal)

        return dfs(root, 0)