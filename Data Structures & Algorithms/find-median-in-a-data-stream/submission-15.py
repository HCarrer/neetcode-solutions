    # ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

    # Output:
    # [null, null, 1.0, null, 2.0, null, 2.0]

    # Explanation:
    # MedianFinder medianFinder = new MedianFinder();
    # medianFinder.addNum(1);    // arr = [1]
    # medianFinder.findMedian(); // return 1.0
    # medianFinder.addNum(3);    // arr = [1, 3]
    # medianFinder.findMedian(); // return 2.0
    # medianFinder.addNum(2);    // arr[1, 2, 3]
    # medianFinder.findMedian(); // return 2.0
        
    # [1]
    # [2,1]
    # [2,2,1]
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
        print("small, large", self.small, self.large)
        if len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2.0
        