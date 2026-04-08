# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # [1,2,3,null,null,4,5] === 1,2,3,N,N,4,5,N,N,N,N
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # [1,2,3] -> "ro1,l2,r3,"
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)

    # 1,2,3,N,N,4,5,N,N,N,N === [1,2,3,null,null,4,5]
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))

        q = deque([root])
        index = 1

        while q:
            node = q.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index+=1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index+=1

        return root



