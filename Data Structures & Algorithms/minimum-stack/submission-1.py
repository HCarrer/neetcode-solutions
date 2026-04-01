class MinStack:

    def __init__(self):
        self.stack = []
        self.pointer = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pointer += 1

    def pop(self) -> None:
        self.stack = self.stack[0:-1]
        self.pointer += 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        values = set(self.stack)
        return min(values)
