class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        edgeList = [[] for i in range(n)]

        for left, right in edges:
            edgeList[left].append(right)
            edgeList[right].append(left)

        visited = set()
        def validate(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in edgeList[node]:
                if neighbor == parent:
                    continue
                if not validate(neighbor, node):
                    return False
            return True

        return validate(0, -1) and len(visited) == n