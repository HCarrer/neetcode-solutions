class Solution:
    def getSqrSum(self, n: int) -> int:
        total = 0
        while n>0:
            alg = n % 10
            total+=alg**2
            n = n // 10
        return total

    def isHappy(self, n: int) -> bool:
        ocur = set()
        while n not in ocur:
            ocur.add(n)
            n = self.getSqrSum(n)
            print(ocur, n)
            if n == 1:
                return True
        return False