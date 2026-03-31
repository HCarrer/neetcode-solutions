class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        windowCount = {}
        longest = 0
        maxF = 0
        for r in range(len(s)):
            windowCount[s[r]] = windowCount.get(s[r], 0) + 1
            
            maxF = max(maxF, windowCount[s[r]])

            while r-l+1 - maxF > k:
                windowCount[s[l]] -= 1
                l += 1
                
            longest = max(longest, r-l+1)
            
        return longest