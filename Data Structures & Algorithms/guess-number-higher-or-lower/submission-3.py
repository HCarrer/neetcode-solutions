# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(1) == 0 or guess(2) == -1:
            return 1
        left, right = 3, n

        while True:
            m = (left + right) // 2
            guessResult = guess(m)
            if guessResult == 0:
                return m
            if guessResult > 0:
                left = m + 1
            elif guessResult < 0:
                right = m - 1
