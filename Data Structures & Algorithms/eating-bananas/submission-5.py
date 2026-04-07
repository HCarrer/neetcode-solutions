class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate,maxRate = 1, max(piles)
        res = maxRate

        while minRate<=maxRate:
            k = (minRate+maxRate)//2 # rate as the average between lower and max rates

            totalTime = 0
            for pile in piles:
                timePerPile = math.ceil(pile/k)
                totalTime+=timePerPile
            if totalTime <= h:
                res = k
                maxRate = k-1
            else:
                minRate = k+1
        return res