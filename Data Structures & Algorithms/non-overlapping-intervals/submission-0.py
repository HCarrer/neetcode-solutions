class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        START, END = 0, 1

        prevEnd = intervals[0][END]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][START]:
                res += 1
            else:
                prevEnd = intervals[i][END]

        return res