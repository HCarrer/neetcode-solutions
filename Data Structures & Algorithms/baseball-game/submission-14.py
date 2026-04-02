class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        scoreStack = []
        for operation in operations:
            print(scoreStack)
            if operation == "C":
                removed = scoreStack.pop()
                total -= int(removed)
            elif operation == "D":
                newScore = int(scoreStack[-1]) * 2
                scoreStack.append(newScore)
                total += newScore
            elif operation == "+":
                top, secondTop = scoreStack[-1], scoreStack[-2]
                newScore = top + secondTop
                scoreStack.append(newScore)
                total += newScore
            else:
                scoreStack.append(int(operation))
                total += int(operation)
        return total