class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = ["r","b","l","t"] #r,b,l,t,r,b,l,t
        dirIndex = 0
        visited = 0
        row=col=0
        res = []
        xBounds = [0, len(matrix[0]) - 1]
        yBounds = [0, len(matrix) - 1]
        while visited < len(matrix) * len(matrix[0]):
            print(direction[dirIndex % 4], matrix[row][col], xBounds, yBounds)
            res.append(matrix[row][col])
            visited+=1
            if direction[dirIndex % 4] == "r":
                if col == xBounds[1]:
                    yBounds[0] += 1
                    dirIndex+=1
                    row+=1
                else:
                    col+=1
            elif direction[dirIndex % 4] == "l":
                if col == xBounds[0]:
                    yBounds[1] -= 1
                    dirIndex+=1
                    row-=1
                else:
                    col-=1
            elif direction[dirIndex % 4] == "b":
                if row == yBounds[1]:
                    xBounds[1] -= 1
                    dirIndex+=1
                    col-=1
                else:
                    row+=1
            elif direction[dirIndex % 4] == "t":
                if row == yBounds[0]:
                    xBounds[0] += 1
                    dirIndex+=1
                    col+=1
                else:
                    row-=1
        return res