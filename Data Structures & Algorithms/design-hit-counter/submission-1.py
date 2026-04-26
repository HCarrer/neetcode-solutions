class HitCounter:

    def __init__(self):
        self.lastHits = deque([])

    def hit(self, timestamp: int) -> None:
        self.lastHits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        validHits = self.lastHits
        while validHits and timestamp - validHits[0] >= 300:
            validHits.popleft()
        return len(validHits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
