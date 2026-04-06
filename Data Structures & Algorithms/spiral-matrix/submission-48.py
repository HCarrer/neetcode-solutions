class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # direction = ["r","b","l","t"] #r,b,l,t,r,b,l,t
        directions = [(0,1), (1,0), (0,-1), (-1,0)] #(x,y)
        dirIndex = 0
        visited = 0
        row=col=0
        res = []
        xBounds = [0, len(matrix[0]) - 1]
        yBounds = [0, len(matrix) - 1]
        while visited < len(matrix) * len(matrix[0]):
            print(row, col)
            res.append(matrix[row][col])
            visited+=1
            if dirIndex % 4 == 0:
                if col == xBounds[1]:
                    yBounds[0] += 1
                    dirIndex+=1
            elif dirIndex % 4 == 1:
                if row == yBounds[1]:
                    xBounds[1] -= 1
                    dirIndex+=1
            elif dirIndex % 4 == 2:
                if col == xBounds[0]:
                    yBounds[1] -= 1
                    dirIndex+=1
            elif dirIndex % 4 == 3:
                if row == yBounds[0]:
                    xBounds[0] += 1
                    dirIndex+=1
            x,y = directions[dirIndex % 4]
            row, col = row + x, col + y
        return res