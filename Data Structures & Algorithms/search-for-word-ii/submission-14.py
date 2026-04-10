class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.index = -1
        self.refs = 0

    def addWord(self, word, i):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.index = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        res = []

        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        # im going to create a dfs function that reads all the neighbours
        # if they have not been visited yet.
        # The visit is going to be tracked by replacing the board cell with *
        # If it matches with the current word, append it to the result
        def getIndex(c):
            return ord(c) - ord('a')

        def dfs(r, c, node):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] == "*" or
                not node.children[getIndex(board[r][c])]
            ):
                return 

            tmp = board[r][c]
            board[r][c] = "*"
            prev = node
            node = node.children[getIndex(tmp)]
            if node.index != -1:
                res.append(words[node.index])
                node.index = -1
                node.refs = -1
                if not node.refs:
                    prev.children[getIndex(tmp)] = None
                    node = None
                    board[r][c] = tmp
                    return

            for direction in directions:
                dr, dc = direction
                dfs(r+dr, c+dc, node)

            board[r][c] = tmp

        # to end i am going to loop through all elements of the grid and start
        # a new dfs in each one of them
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)

        return res

