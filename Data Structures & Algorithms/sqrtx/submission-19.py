class Solution:
    def mySqrt(self, x: int) -> int:
        # 1, 4, 9, 16, 25, 36
        # 3, 5, 7, 9, 11, 13

        num = 1
        paRatio = 3
        res = 1
        while True:
            if num > x:
                return res-1
            elif num == x:
                return res
            sqr = num+paRatio
            paRatio+=2
            num = sqr
            res += 1
        # return res if num == x else res-1