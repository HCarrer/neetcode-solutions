"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for index, interval in enumerate(intervals):
            current = interval
            if index == len(intervals) - 1:
                return True
            nextInterval = intervals[index+1]
            if current.end > nextInterval.start:
                return False
        return True
                