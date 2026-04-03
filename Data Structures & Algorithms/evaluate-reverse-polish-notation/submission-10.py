class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valuesStack = []

        for token in tokens:
            if token in ["+","-","*","/"]:
                second, first = valuesStack.pop(), valuesStack.pop()
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                elif token == "/":
                    result = int(float(first) / second)
                valuesStack.append(result)
            else:
                valuesStack.append(int(token))

        return valuesStack[-1]