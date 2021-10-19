class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        lp = len(prices)
        buy = [float('-inf') for _ in range(lp)]
        sell = [0 for _ in range(lp)]
        for i,price in enumerate(prices):
            if i == 0:
                buy[0] = -price
                sell[0] = max(sell[0], buy[0] + price - fee)
            buy[i] = max(buy[i-1], sell[i-1] - price)
            sell[i] = max(sell[i-1], buy[i] + price - fee)
        return sell[-1]