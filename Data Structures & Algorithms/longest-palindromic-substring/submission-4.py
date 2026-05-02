class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        n = len(s)

        if n == 1:
            return s

        def isPalyndrome(text):
            reversedText = text[::-1]
            return text == reversedText
            # l, r = 0, len(text) - 1

            # while l<=r:
            #     if text[l] != text[r]:
            #         return False
            #     l+=1
            #     r-=1
            # return True

        leftIndex, rightIndex = 0, n-1

        while leftIndex < n and leftIndex <= rightIndex:
            if rightIndex == leftIndex:
                leftIndex += 1
                rightIndex = n-1
            
            if s[rightIndex] == s[leftIndex]:
                string = s[leftIndex : rightIndex + 1]
                if isPalyndrome(string):
                    if len(string) > len(longest):
                        longest = string
            
            rightIndex -= 1


        # for leftIndex in range(n):
        #     for rightIndex in range(n-1, leftIndex, -1):
        #         if s[rightIndex] != s[leftIndex]:
        #             continue

        #         string = s[leftIndex : rightIndex + 1]
        #         if isPalyndrome(string):
        #             if len(string) > len(longest):
        #                 longest = string

        return longest