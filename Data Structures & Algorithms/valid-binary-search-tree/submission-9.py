# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def dfs(node: Optional[TreeNode], left, right) -> bool:
        #     if not node:
        #         return True

        #     val = node.val
        #     if left >= val or right <= val:
        #         return False
                
            
        #     return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        # return dfs(root, float("-inf"), float("inf"))

        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()

            if left >= node.val or right <= node.val:
                return False

            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
        return True