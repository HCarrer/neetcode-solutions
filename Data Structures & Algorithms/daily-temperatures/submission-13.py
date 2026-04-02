class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for index in range(len(temperatures)):
            comparator = index
            found = False
            while comparator < len(temperatures):
                if temperatures[comparator] <= temperatures[index]:
                    comparator += 1
                else:
                    found = True
                    break
            if found:
                res[index] = comparator - index

        return res