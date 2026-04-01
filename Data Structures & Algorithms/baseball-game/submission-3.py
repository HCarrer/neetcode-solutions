class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        pointer = 0
        for value in operations:
            if value == "C":
                points.pop()
                pointer -= 1
            elif value == "D":
                points.append(2*int(points[pointer-1]))
                pointer += 1
            elif value == "+":
                points.append(int(points[pointer-1])+int(points[pointer-2]))
                pointer += 1
            else:
                points.append(int(value))
                pointer += 1
        
        res = 0
        for point in points:
            res += point
        return res