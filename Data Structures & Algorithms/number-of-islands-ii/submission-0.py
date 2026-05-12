class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ROWS, COLS = m, n
        grid = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        WATER, LAND = 0, 1
        
        totalIslands = 0

        def dfs(r, c, visited):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == WATER or
                (r,c) in visited
            ):
                return False

            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited)
            return True

        def countIslands():
            count = 0
            visited = set()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == LAND:
                        if dfs(r,c,visited):
                            count+=1
            return count

        res = []
        for r, c in positions:
            grid[r][c] = 1
            res.append(countIslands())

        return res