class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        heapq.heapify_max(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush_max(self.small, num)

        # if large has 2 or more elements than small
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)
        # if small has 2 or more elements than large
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2.0
        