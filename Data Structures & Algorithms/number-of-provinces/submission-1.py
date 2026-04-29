class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #   [1,1,0]
        #   [1,1,0]
        #   [0,0,1]



        #   [1,0,1]
        #   [0,1,1]
        #   [1,1,1]

        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)

        return provinces
