class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            buy, sell = prices[l], prices[r]
            if buy < sell:
                profit = sell - buy
                res = max(res, profit)
            else:
                l = r
            r +=1
        return res