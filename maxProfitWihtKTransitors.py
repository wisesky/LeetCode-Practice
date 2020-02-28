import math
class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        #k = min(k, len(prices)//2)
        if prices == []:
            return 0
        if k == 0:
            return 0
        if k >= len(prices)//2:
            profit, prev = 0, prices[0]
            for i in range(1,len(prices)):
                if prices[i] >= prices[i-1]:
                    profit = profit + prices[i]-prices[i-1]
            return profit    
        # solution #1
        """ maxProfit = [0 for i in range(k+1)]
        lowestBuyPrice = [math.inf for i in range(k)]
        
        for price in prices:
            for i in range(k):
                #maxProfit[i] = max(maxProfit[i], price - lowestBuyPrice[i])
                lowestBuyPrice[i] = min(lowestBuyPrice[i], price - maxProfit[i+1])
                maxProfit[i] = max(maxProfit[i], price - lowestBuyPrice[i])
        return maxProfit[0] """
        # solution #2
        buy = [float('-inf') for _ in range(k)]
        sell = [0 for _ in range(k)]

        for price in prices:
            buy[0] = max(buy[0], -price)
            sell[0] = max(sell[0], buy[0] + price)
            for i in range(1, k):
                buy[i] = max(buy[i], sell[i-1] - price)
                sell[i] = max(sell[i], buy[i] + price)

        return sell[-1]