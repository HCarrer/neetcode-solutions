class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        START, END = 0, 1
        intervals.sort(key=lambda x: x[START])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][END]

            if start <= lastEnd:
                res[-1][END] = max(lastEnd, end)
            else:
                res.append([start, end])

        return res