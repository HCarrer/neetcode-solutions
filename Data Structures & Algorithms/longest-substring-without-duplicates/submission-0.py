class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        subString = set()
        longest = 0
        
        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l+=1
            subString.add(s[r])
            longest = max(longest, r-l+1)
            
        return longest