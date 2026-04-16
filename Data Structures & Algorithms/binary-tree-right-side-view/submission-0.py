# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        # apply bfs so it always reads the entire level of the tree
        # push the right most element of the deque in the res array

        res = []

        q = deque([(root, 0)])
        levels = {}
        while q:
            node, level = q.popleft()
            print(node.val, level)
            if not level in levels:
                levels[level] = []
            levels[level].append(node.val)
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            
        for level in levels.values():
            if not level:
                continue
            rightMost = level.pop()
            res.append(rightMost)

        return res