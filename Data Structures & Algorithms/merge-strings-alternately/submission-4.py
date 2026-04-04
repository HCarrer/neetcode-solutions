class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        size1, size2 = len(word1), len(word2)
        
        for i in range(max(size1, size2)):
            if i < size1:
                res += word1[i]
            if i < size2:
                res += word2[i]
        return res