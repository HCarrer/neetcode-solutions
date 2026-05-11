"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        roomsInUse = []

        for interval in intervals:
            if roomsInUse and roomsInUse[0] <= interval.start:
                heapq.heappop(roomsInUse)
            heapq.heappush(roomsInUse, interval.end)

        return len(roomsInUse)