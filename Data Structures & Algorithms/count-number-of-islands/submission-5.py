class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        land = "1"
        water = "0"

        def dfs(r,c):
            if (
                r<0 or c<0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == water
            ):
                return
            
            grid[r][c] = water
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == land:
                    dfs(r,c)
                    islands+=1

        return islands