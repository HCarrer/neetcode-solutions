class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        q = deque([0])

        numOfCoins = 0
        seen = [False] * (amount + 1)
        seen[0] = True

        while q:
            numOfCoins += 1
            for x in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return numOfCoins
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1