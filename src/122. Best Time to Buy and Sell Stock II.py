from typing import List
class Solution:
    # unlimited transactions
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        r = []
        for i, price in enumerate(prices):
            if i == 0 :
                pre = price
                curlow = float('inf')
                cms = 0
            elif pre > price:
                r.append(cms)
                cms = 0
                curlow = float('inf')
            
            cms = max(cms, price - curlow)
            curlow = min(curlow, price)
            pre = price
            # print()

        r.append(cms)
        return sum(r)

if __name__ == "__main__":
    so = Solution()
    l = [7,1,5,3,6,4]
    # l = [1,2,3,4,5]
    print(so.maxProfit(l))