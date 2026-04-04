class Solution:

    def __init__(self, w: List[int]):
        self.indexes = []
        for index, weight in enumerate(w):
            while weight:
                self.indexes.append(index)
                weight -= 1

    def pickIndex(self) -> int:
        return self.indexes[random.randrange(0, len(self.indexes))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()