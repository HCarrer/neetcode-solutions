class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] == "X" or
                board[r][c] == "T"
            ):
                return

            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][COLS-1] == "O":
                dfs(row, COLS-1)

        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col)
            if board[ROWS-1][col] == "O":
                dfs(ROWS-1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
