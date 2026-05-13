class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        zeroes = []

        for r in range(ROWS):
            for c in range(COLS):
                if not matrix[r][c]:
                    zeroes.append((r,c))

        for zero in zeroes:
            zeroR, zeroC = zero
            for r in range(ROWS):
                matrix[r][zeroC] = 0
            for c in range(COLS):
                matrix[zeroR][c] = 0