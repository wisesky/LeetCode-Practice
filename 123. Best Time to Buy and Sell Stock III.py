from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        sell = [0,0]
        buy = [float('-inf'), float('-inf')]

        for price in prices:
            # for i in range(1,-1,-1):
            #     sell[i] = max(sell[i], buy[i] + price)
            #     buy[i] = max(buy[i], sell[i-1] - price)
            sell[1] = max(sell[1], buy[1] + price)
            buy[1] = max(buy[1], sell[0] - price)
            sell[0] = max(sell[0] , buy[0] + price)
            buy[0] = max(buy[0], - price)
            print(sell[1],buy[1],sell[0],buy[0])
        return sell[1]

if __name__ == "__main__":
    so = Solution()
    l = [3,3,5,0,0,3,1,4]
    # l = [1,2,3,4,5]
    print(so.maxProfit(l))