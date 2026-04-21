class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        targetRow = -1

        rowLeft, rowRight = 0, ROWS - 1

        while rowLeft <= rowRight:
            m = (rowLeft+rowRight) // 2
            if matrix[m][-1] < target:
                rowLeft = m + 1
            elif matrix[m][0] > target:
                rowRight = m - 1
            else:
                targetRow = m
                break
        
        l,r = 0, COLS-1
        while l<=r:
            m = (l+r) // 2
            if matrix[targetRow][m] == target:
                return True
            if matrix[targetRow][m] < target:
                l = m + 1
            elif matrix[targetRow][m] > target:
                r = m - 1
        return False