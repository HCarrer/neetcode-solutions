class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for index in range(len(temperatures)):
            comparator = index
            found = False
            while comparator < len(temperatures):
                if temperatures[comparator] <= temperatures[index]:
                    print(temperatures[comparator], temperatures[index])
                    # res[index] += 1
                    comparator += 1
                else:
                    found = True
                    print('breaking')
                    break
            if found:
                res[index] = comparator - index
            print('-------')

        return res