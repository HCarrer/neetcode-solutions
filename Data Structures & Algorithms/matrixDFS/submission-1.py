LAND = 0
ROCK = 1

class Solution:
    def countPaths( Falseself, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, visited):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or 
                (r,c) in visited or
                grid[r][c] == ROCK
            ):
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1

            visited.add((r,c))
            
            uniquePaths = 0

            uniquePaths += dfs(r+1,c,visited)
            uniquePaths += dfs(r-1,c,visited)
            uniquePaths += dfs(r,c+1,visited)
            uniquePaths += dfs(r,c -1,visited)

            visited.remove((r,c))
            return uniquePaths

        return dfs(0,0,set())