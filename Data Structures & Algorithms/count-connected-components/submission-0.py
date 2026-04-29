class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        x = {i: [] for i in range(n)}

        for a, b in edges:
            x[a].append(b)
            x[b].append(a)


        connected = 0

        visited = [False] * n

        def checkConnection(edge):
            for nei in x[edge]:
                if not visited[nei]:
                    visited[nei] = True
                    checkConnection(nei)

        for edge in range(n):
            if not visited[edge]:
                visited[edge] = True
                checkConnection(edge)
                connected += 1

        return connected