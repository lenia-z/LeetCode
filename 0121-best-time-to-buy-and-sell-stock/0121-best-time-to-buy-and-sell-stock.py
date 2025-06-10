class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]

        for p in prices[1:]:
            # if p < buy:
            #     buy = p
            buy = min(buy, p)
            # profit = p - buy
            # if profit > maxProfit:
            #     maxProfit = profit
            maxProfit = max(maxProfit, p - buy)

        return maxProfit 