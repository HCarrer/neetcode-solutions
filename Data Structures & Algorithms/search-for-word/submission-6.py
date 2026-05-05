class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1),(0,-1),(1, 0),(-1, 0)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if len(word) == i:
                return True

            if (r < 0 or r>=ROWS or
                c < 0 or c>=COLS or
                visited[r][c] or
                board[r][c] != word[i]):
                return
            # mark as visited
            visited[r][c] = True
            res = []
            for dr, dc in directions:
                res.append(dfs(r+dr, c+dc, i+1))
            visited[r][c] = False
            return True in res


        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
