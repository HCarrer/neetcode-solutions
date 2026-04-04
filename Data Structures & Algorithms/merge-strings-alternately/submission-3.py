class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        while word1 and word2:
            print(word1, word2)
            pop1, word1 = word1[0], word1[1:]
            pop2, word2 = word2[0], word2[1:]
            res += pop1+pop2
        if word1:
            res += word1
        if word2:
            res += word2
        return res