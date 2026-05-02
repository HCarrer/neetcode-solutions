class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.resIndex = 0
        self.resLength = 0
        n = len(s)

        def checkPalyndrome(index, isEven):
            left, right = index, index + 1 if isEven else index

            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > self.resLength:
                    self.resLength = right - left + 1
                    self.resIndex = left
                left -= 1
                right += 1

        for i in range(n):
            checkPalyndrome(i, False)
            checkPalyndrome(i, True)

        return s[self.resIndex : self.resIndex + self.resLength]

        