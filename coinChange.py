class Solution:
    dp = [0]
    
    # making the dp array an instance variable would cause TLE
    """ def __init__(self):
        self.dp = [0]
 """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #dp = self.dp + [float('inf') for _ in range(amount+1)]
        dp = self.dp
        dp += [float('inf') for _ in range(amount+1)]
        for coin in sorted(coins):
            for i in range(1, amount+1):
                dp[i] = min(dp[i], (dp[i-coin] if i >= coin else float('inf'))+1)

        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coin = [1,3,5]
    so = Solution()
    res = so.coinChange(coin, 11)
    print(res)