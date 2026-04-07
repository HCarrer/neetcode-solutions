class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBananas = 0
        for pile in piles:
            totalBananas+=pile
        minRate,maxRate = math.ceil(totalBananas/h), max(piles)
        print(minRate, maxRate)
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