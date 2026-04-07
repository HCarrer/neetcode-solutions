class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = []
        self.uniques = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for num in self.nums:
            if num in self.uniques and self.uniques.get(num, False):
               return num 
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.uniques:
            self.uniques[value] = False
        else:
            self.uniques[value] = True


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
