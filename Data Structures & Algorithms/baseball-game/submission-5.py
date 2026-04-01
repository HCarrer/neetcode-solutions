class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for value in operations:
            if value == "C":
                points.pop()
            elif value == "D":
                points.append(2*int(points[-1]))
            elif value == "+":
                points.append(int(points[-1])+int(points[-2]))
            else:
                points.append(int(value))
        
        res = 0
        for point in points:
            res += point
        return res