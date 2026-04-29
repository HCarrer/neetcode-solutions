class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        n = len(intervals)
        l, r = 0, n - 1

        START, END = 0, 1


        while l<=r:
            m = (l + r) // 2
            if intervals[m][START] < newInterval[START]:
                l = m + 1
            else:
                r = m - 1

        intervals.insert(l, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][END] < interval[START]:
                res.append(interval)
            else:
                res[-1][END] = max(res[-1][END], interval[END])

        return res