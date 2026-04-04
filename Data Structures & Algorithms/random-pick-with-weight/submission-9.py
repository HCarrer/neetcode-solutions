class Solution:

    def __init__(self, w: List[int]):
        self.indexes = []
        maxIndex = max(w)
        print(w)
        for index, weight in enumerate(w):
            while weight:
                self.indexes.append(index)
                weight -= 1
        # for diffWeight in w:
        #     print(diffWeight)
        #     index, weight = diffWeight[0], diffWeight[1]
        #     while weight:
        #         self.indexes.append(index)
        #         weight -= 1
        # for n in range(maxIndex):
        #     self.indexes.append(n)

    def pickIndex(self) -> int:
        return self.indexes[random.randrange(0, len(self.indexes))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()