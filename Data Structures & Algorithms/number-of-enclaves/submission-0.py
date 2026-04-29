class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # step 1: for each wall (t,r,b,l) perform dfs transforming 1s into 0s
        # step 2: for each cell in the grid, add 1 if is land

        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c):
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                return

            grid[r][c] = 0
            for dr, dc in DIRECTIONS:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += 1

        return res