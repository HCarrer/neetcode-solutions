class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def find(self, word, i, j):
        cur = self.root
        for idx in range(i, j+1):
            if not word[idx] in cur.children:
                return False
            cur = cur.children[word[idx]]
        return cur.endOfWord

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # step 1: create and populate Trie
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True


        maxWordLen = 0
        for w in wordDict:
            maxWordLen = max(maxWordLen, len(w))

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i+maxWordLen)):
                if trie.find(s, i, j):
                    dp[i] = dp[j+1]
                    if dp[i]:
                        break

        print(dp)

        return dp[0]
