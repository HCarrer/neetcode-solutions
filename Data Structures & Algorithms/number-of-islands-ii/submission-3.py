class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = 0

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ROWS, COLS = m, n
        grid = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        WATER, LAND = 0, 1
        
        dsu = Union(m*n)

        res = []

        for r, c in positions:
            if grid[r][c] == LAND:
                res.append(dsu.count)
                continue

            grid[r][c] = LAND
            dsu.count += 1

            for dr, dc in directions:
                nr, nc = dr+r, dc+c

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == LAND:
                    dsu.union(r*n + c, nr*n + nc)

            res.append(dsu.count)

        return res