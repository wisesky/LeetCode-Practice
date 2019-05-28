class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        #self.n = n
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for l in range(1,n):
            dp[l][l+1] = l
        for gap in range(2,n):
            for i in range(1, n+1-gap):
                j = i + gap
                dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in range(i+1,j))

        return dp[1][n]
