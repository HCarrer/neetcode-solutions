class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        totalWhites, totalBlacks = 0, 0

        for i in range(k):
            if blocks[i] == "B":
                totalBlacks += 1
            else:
                totalWhites += 1

        minWhites = totalWhites

        ptr = k
        while ptr < len(blocks):
            if blocks[ptr] == "B" and blocks[ptr-k] == "W":
                totalBlacks += 1
                totalWhites -= 1
            elif blocks[ptr] == "W" and blocks[ptr-k] == "B":
                totalBlacks -= 1
                totalWhites += 1
            minWhites = min(minWhites, totalWhites)
            ptr += 1

        return minWhites