class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        # set left and right pointers
        l, r = 0, 1

        maxProfit = 0

        # "You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it."
        # so with that i know that the purchase cannot be done after the selling
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]

            profit = sell - buy
            if profit > 0:
                maxProfit = max(maxProfit, profit)

            else:
                l = r
        
            r+=1
        return maxProfit
