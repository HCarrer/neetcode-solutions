# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # empty tree is always a subtree
            return True

        if subRoot and not root:
            return False

        if self.sameTree(root, subRoot): # if the same, return True
            return True

        # check for left and right nodes
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if both are empty, they are the same
        if not root and not subRoot:
            return True

        # if one is empty and the other one is not, return False
        if ((not root and subRoot) or (root and not subRoot)):
            return False

        # if the values differ at the node, return False
        if root.val != subRoot.val:
            return False

        # check for left and right nodes
        return (self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right))

                