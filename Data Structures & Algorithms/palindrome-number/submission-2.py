class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        length = len(strX)

        l,r = 0, length - 1
        while l<r:
            if strX[l] != strX[r]:
                return False
            l+=1
            r-=1
        return True