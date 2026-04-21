LAND = 0
ROCK = 1

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(0,-1), (1,0),(-1,0)]

        q = deque([(0,0)])
        visited = set((0,0))
        shortestLength = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return shortestLength

                for direction in directions:
                    dr, dc = direction
                    if (r+dr < 0 or c+dc < 0 or
                        r+dr == ROWS or c+dc == COLS or
                        (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == ROCK
                    ):
                        continue

                    q.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
            shortestLength += 1

        return -1