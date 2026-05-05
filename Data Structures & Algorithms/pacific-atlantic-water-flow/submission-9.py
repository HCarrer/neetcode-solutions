class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        
        def dfs(r, c, visited, prevHeight):
            if ((r,c) in visited or
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, visited, heights[r][c])

        pac, atl = set(), set()
            
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
            
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    res.append([row,col])

        return res
