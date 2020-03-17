class Solution:
    def maxProfit(self, prices) :
        curlow = float('inf')
        cms = 0
        for price in prices:
            cms = max(cms, price - curlow)
            curlow = min(curlow, price)
            print()
        return cms
            
if __name__ == "__main__":
    so = Solution()
    l = [7,1,5,3,6,4]
    print(so.maxProfit(l))
