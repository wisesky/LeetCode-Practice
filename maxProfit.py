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
        if k >= len(prices)//2:
            profit, prev = 0, prices[0]
            for i in range(1,len(prices)):
                if prices[i] >= prices[i-1]:
                    profit = profit + prices[i]-prices[i-1]
            return profit    
        
        maxProfit = [0 for i in range(k+1)]
        lowestBuyPrice = [math.inf for i in range(k)]
        
        for price in prices:
            for i in range(k):
                maxProfit[i] = max(maxProfit[i], price - lowestBuyPrice[i])
                lowestBuyPrice[i] = min(lowestBuyPrice[i], price - maxProfit[i+1])
        return maxProfit[0]
        