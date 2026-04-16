class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0 # mark as visited to avoid duplicates
            count = 1
            for direction in directions:
                dr, dc = direction
                count += dfs(r+dr,c+dc)
            return count

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                count = dfs(r,c)
                maxArea = max(maxArea, count)

        return maxArea